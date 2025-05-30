import os
from yt_dlp import YoutubeDL
from typing import Optional

class AudioDownloader:
    def __init__(self, output_dir: str = "/Users/ranjana/Documents/codes/personal_workspace/Scriptive/data/raw/audio"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def download_audio(self, video_url: str, filename: Optional[str] = None) -> str:
        """Downloads audio from a YouTube video as .mp3 using yt_dlp Python API"""
        # Define output filename template
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(self.output_dir, '%(id)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
            'noplaylist': True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            video_id = info_dict.get("id")
            filename = f"{video_id}.mp3"
            file_path = os.path.join(self.output_dir, filename)

            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Expected output {file_path} not found.")

            return file_path

if __name__ == "__main__":
    downloader = AudioDownloader()
    audio_path = downloader.download_audio("https://www.youtube.com/watch?v=ZC98ZK6Ivug")
    print(f"Audio downloaded at: {audio_path}")
