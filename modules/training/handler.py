import os
import argparse

from modules.ingestion.youtube_scraper import YouTubeScraper
from modules.ingestion.audio_downloader import AudioDownloader
from modules.transcription.transcribe import AssemblyTranscriber
from modules.style.handler import StyleProfileBuilder

def run_style_extraction(channel_handle: str, num_videos: int):
    print(f"[INFO] Starting style extraction for {channel_handle}...")

    # Step 1: Scrape
    scraper = YouTubeScraper()
    channel_id = scraper.get_channel_id(channel_handle)
    videos = scraper.get_channel_videos(channel_id, max_results=num_videos)

    print(f"[INFO] Fetched {len(videos)} videos.")

    # Step 2: Download and Transcribe
    downloader = AudioDownloader()
    transcriber = AssemblyTranscriber()
    transcripts = []

    for video in videos:
        video_id = video["video_id"]
        title = video["title"]
        print(f"[INFO] Processing: {title}")

        try:
            audio_path = downloader.download_audio(video["video_url"], filename=video_id)
            transcript_path = f"data/processed/transcripts/{video_id}.txt"
            result = transcriber.transcribe(audio_path, save_path=transcript_path)
            transcripts.append(result["text"])
        except Exception as e:
            print(f"[WARN] Failed to process video {video_id}: {e}")
            continue

    if not transcripts:
        print("[ERROR] No transcripts found. Aborting.")
        return

    # Step 3: Combine and Build Style Profile
    full_text = "\n\n".join(transcripts)
    profile_builder = StyleProfileBuilder()
    profile = profile_builder.build_profile(full_text)

    # Step 4: Save style profile
    channel_name_safe = channel_handle.strip("@").replace(" ", "_").lower()
    output_path = f"data/processed/style_profiles/{channel_name_safe}.json"
    profile_builder.save_profile(profile, output_path)

    print(f"[SUCCESS] Style profile saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run style extraction for a YouTube channel.")
    parser.add_argument("--channel", type=str, required=True, help="YouTube handle or name")
    parser.add_argument("--num_videos", type=int, default=10, help="Number of videos to extract")
    args = parser.parse_args()

    run_style_extraction(args.channel, args.num_videos)
