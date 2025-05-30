import os
import time
import requests
from typing import Dict
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

ASSEMBLY_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
TRANSCRIBE_ENDPOINT = "https://api.assemblyai.com/v2/transcript"
UPLOAD_ENDPOINT = "https://api.assemblyai.com/v2/upload"

class AssemblyTranscriber:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or ASSEMBLY_API_KEY
        if not self.api_key:
            raise ValueError("Missing AssemblyAI API key.")

        self.headers = {
            "authorization": self.api_key,
            "content-type": "application/json"
        }

    def upload_audio(self, file_path: str) -> str:
        """Uploads audio to AssemblyAI and returns upload_url."""
        with open(file_path, 'rb') as f:
            response = requests.post(
                UPLOAD_ENDPOINT,
                headers={"authorization": self.api_key},
                data=f
            )
        response.raise_for_status()
        return response.json()['upload_url']

    def request_transcription(self, upload_url: str) -> str:
        """Submits transcription request and returns transcript ID."""
        data = {
            "audio_url": upload_url,
            "speaker_labels": False,
            "auto_chapters": False
        }
        response = requests.post(TRANSCRIBE_ENDPOINT, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()['id']

    def poll_transcription(self, transcript_id: str, sleep_interval: int = 5) -> Dict:
        """Polls AssemblyAI until transcription is complete."""
        polling_url = f"{TRANSCRIBE_ENDPOINT}/{transcript_id}"

        while True:
            response = requests.get(polling_url, headers=self.headers)
            response.raise_for_status()
            status = response.json()['status']

            if status == 'completed':
                return response.json()
            elif status == 'failed':
                raise RuntimeError("Transcription failed")
            time.sleep(sleep_interval)

    def transcribe(self, file_path: str, save_path: Optional[str] = None) -> Dict:
        """
        One-shot transcribe pipeline: upload, request, poll, return text + words.
        Optionally saves transcript to a text file.
        """
        upload_url = self.upload_audio(file_path)
        transcript_id = self.request_transcription(upload_url)
        transcript_data = self.poll_transcription(transcript_id)

        text = transcript_data["text"]
        segments = transcript_data.get("words", [])

        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(text)

        return {
            "text": text,
            "segments": segments
        }


if __name__ == "__main__":
    transcriber = AssemblyTranscriber()
    audio_file = "/Users/ranjana/Documents/codes/personal_workspace/Scriptive/data/raw/audio/ZC98ZK6Ivug.mp3"
    output_file = "/Users/ranjana/Documents/codes/personal_workspace/Scriptive/data/processed/transcripts/ZC98ZK6Ivug.txt"
    result = transcriber.transcribe(audio_file, save_path=output_file)

    print("--- TEXT ---\n")
    print(result["text"])

    print("\n--- SEGMENTS ---")
    for word in result["segments"][:5]:
        print(f"{word['start']} - {word['end']}: {word['text']}")

