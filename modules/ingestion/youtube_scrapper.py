import os
import requests
from typing import List, Dict, Optional
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
YOUTUBE_API_BASE = "https://www.googleapis.com/youtube/v3"

class YouTubeScraper:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or YOUTUBE_API_KEY
        if not self.api_key:
            raise ValueError("YouTube API key not found. Set YOUTUBE_API_KEY in env.")

    def get_channel_id(self, handle_or_url: str) -> str:
        """Fetch channel ID from handle or full URL"""
        if "@" in handle_or_url:
            query = handle_or_url.replace("@", "")
        else:
            query = handle_or_url

        url = f"{YOUTUBE_API_BASE}/search?{urlencode({'part': 'snippet','q': query,'type': 'channel', 'key': self.api_key })}"

        response = requests.get(url)
        response.raise_for_status()

        items = response.json().get("items", [])
        if not items:
            raise ValueError(f"No channel found for: {handle_or_url}")

        return items[0]["snippet"]["channelId"]

    def get_channel_videos(self, channel_id: str, max_results: int = 20) -> List[Dict]:
        """Returns basic metadata of latest videos"""
        search_url = f"{YOUTUBE_API_BASE}/search?{urlencode({'key': self.api_key, 'channelId': channel_id, 'part': 'snippet', 'maxResults': max_results, 'order': 'date'})}"

        res = requests.get(search_url)
        res.raise_for_status()
        items = res.json().get("items", [])

        videos = []
        for item in items:
            if item["id"]["kind"] != "youtube#video":
                continue

            videos.append({
                "video_id": item["id"]["videoId"],
                "title": item["snippet"]["title"],
                "description": item["snippet"]["description"],
                "published_at": item["snippet"]["publishedAt"],
                "channel_title": item["snippet"]["channelTitle"],
                "video_url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            })

        return videos

if __name__ == "__main__":
    from pprint import pprint

    scraper = YouTubeScraper()
    channel_id = scraper.get_channel_id("@veritasium")
    videos = scraper.get_channel_videos(channel_id, max_results=5)
    pprint(videos)
