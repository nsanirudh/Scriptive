import re
import unicodedata

def remove_non_speech(text: str) -> str:
    """Removes filler tags like [Music], (Applause), etc."""
    return re.sub(r'\[.*?\]|\(.*?\)', '', text)

def remove_emojis(text: str) -> str:
    """Removes emojis and non-text symbols"""
    return ''.join(
        c for c in text
        if unicodedata.category(c)[0] != 'So'
    )

def normalize_whitespace(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()

def clean_transcript(text: str, remove_emoji: bool = True) -> str:
    text = remove_non_speech(text)
    if remove_emoji:
        text = remove_emojis(text)
    text = normalize_whitespace(text)
    return text

if __name__ == "__main__":
    sample = "This is a test 😊 [Music] with some    irregular   spacing and (Applause)"
    cleaned = clean_transcript(sample)
    print("CLEANED:\n", cleaned)
