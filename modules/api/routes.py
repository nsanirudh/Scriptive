from fastapi import APIRouter, UploadFile, File, Form
from typing import List, Optional

from modules.training.handler import run_style_extraction
from modules.training.embedder import embed_channel_transcripts
from modules.prediction.handler import run_prediction

router = APIRouter()

@router.post("/train/style")
def train_style_profile(channel_handle: str = Form(...), num_videos: int = Form(10)):
    """
    Train style profile for a given YouTube channel.
    """
    run_style_extraction(channel_handle, num_videos)
    return {"message": f"Style profile created for {channel_handle}"}


@router.post("/train/embed")
def index_transcripts(channel_id: str = Form(...)):
    """
    Index previously transcribed videos for a channel into Qdrant.
    """
    embed_channel_transcripts(channel_id)
    return {"message": f"Transcript chunks embedded for channel {channel_id}"}


@router.post("/predict/upload-context")
def upload_context(files: List[UploadFile] = File(...)) -> dict:
    """
    Accept and ingest user documents. Saves to temp and returns text.
    """
    from modules.prediction.doc_ingest import ingest_documents
    from modules.prediction.doc_embedder import UserDocEmbedder

    file_paths = []
    for file in files:
        path = f"data/raw/user_docs/{file.filename}"
        with open(path, "wb") as f:
            f.write(file.file.read())
        file_paths.append(path)

    text = ingest_documents(file_paths)
    embedder = UserDocEmbedder()
    collection = embedder.embed_user_text(text)

    return {
        "message": "Documents ingested and indexed",
        "collection_name": collection
    }


@router.post("/predict/script")
def generate_script(
    topic: str = Form(...),
    channel_id: str = Form(...),
    tone: str = Form("educational"),
    audience: str = Form("general"),
    length: str = Form("medium"),
    collection_name: Optional[str] = Form(None)
):
    """
    Generates a script using topic + style + (optional) user document context.
    """
    from modules.prediction.retriever import Retriever
    from modules.prediction.prompt_builder import build_generation_prompt
    from modules.prediction.generator import ScriptGenerator
    import json
    import os

    retriever = Retriever()
    context = retriever.retrieve_relevant_chunks(
        collection_name or channel_id,
        query=topic,
        top_k=5
    )

    profile_path = f"data/processed/style_profiles/{channel_id}.json"
    if not os.path.exists(profile_path):
        return {"error": "Style profile not found"}
    style_profile = json.load(open(profile_path))

    prompt = build_generation_prompt(
        topic=topic,
        style_profile=style_profile,
        context_chunks=context,
        audience=audience,
        tone=tone,
        length=length
    )

    generator = ScriptGenerator()
    output = generator.generate_script(prompt, topic=topic)

    return {
        "topic": topic,
        "style_channel": channel_id,
        "script": output
    }
