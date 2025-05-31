import argparse
import json
import os
from pathlib import Path

from modules.prediction.doc_ingest import ingest_documents
from modules.prediction.doc_embedder import UserDocEmbedder
from modules.prediction.retriever import Retriever
from modules.prediction.prompt_builder import build_generation_prompt
from modules.prediction.generator import ScriptGenerator

STYLE_PROFILE_DIR = "data/processed/style_profiles"

def run_prediction(
    topic: str,
    channel_id: str,
    user_docs: list = None,
    tone: str = "educational",
    audience: str = "general",
    length: str = "medium"
):
    # Step 1: Get context chunks
    if user_docs:
        print(f"[INFO] Ingesting user documents: {user_docs}")
        text = ingest_documents(user_docs)
        embedder = UserDocEmbedder()
        collection = embedder.embed_user_text(text)
        retriever = Retriever()
        context_chunks = retriever.retrieve_relevant_chunks(collection, topic, top_k=5)
    else:
        print(f"[INFO] Retrieving from creator index: {channel_id}")
        retriever = Retriever()
        context_chunks = retriever.retrieve_relevant_chunks(channel_id, topic, top_k=5)

    # Step 2: Load style profile
    profile_path = os.path.join(STYLE_PROFILE_DIR, f"{channel_id}.json")
    if not os.path.exists(profile_path):
        raise FileNotFoundError(f"Style profile not found at: {profile_path}")
    style_profile = json.load(open(profile_path))

    # Step 3: Build prompt
    prompt = build_generation_prompt(
        topic=topic,
        style_profile=style_profile,
        context_chunks=context_chunks,
        audience=audience,
        tone=tone,
        length=length
    )

    # Step 4: Generate output
    generator = ScriptGenerator()
    output = generator.generate_script(prompt, topic=topic)

    # Step 5: Done
    print("\n" + "="*60 + "\n")
    print(output)
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run prediction pipeline for a new script.")
    parser.add_argument("--topic", type=str, required=True, help="Topic for the script")
    parser.add_argument("--channel_id", type=str, required=True, help="Channel ID for style profile and vector index")
    parser.add_argument("--docs", nargs="*", help="Optional list of user documents (PDF, DOCX, TXT)")
    parser.add_argument("--tone", type=str, default="educational")
    parser.add_argument("--audience", type=str, default="general")
    parser.add_argument("--length", type=str, default="medium")

    args = parser.parse_args()

    run_prediction(
        topic=args.topic,
        channel_id=args.channel_id,
        user_docs=args.docs,
        tone=args.tone,
        audience=args.audience,
        length=args.length
    )

# python -m modules.prediction.handler \
#   --topic "Entropy and Black Holes" \
#   --channel_id veritasium \
#   --docs data/raw/user_docs/Black_Holes_and_Entropy.pdf \
#   --tone dramatic \
#   --audience "college physics students" \
#   --length long
