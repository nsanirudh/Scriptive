from textblob import TextBlob
import nltk
from nltk.tokenize import sent_tokenize
from typing import Dict, List

nltk.download("punkt", quiet=True)

def analyze_tone(text: str) -> Dict:
    """
    Computes polarity ([-1,1]) and subjectivity ([0,1]) across sentences.
    Returns average and arc (list of values).
    """
    sentences = sent_tokenize(text)
    if not sentences:
        return {
            "average_polarity": 0.0,
            "average_subjectivity": 0.0,
            "tone_arc": []
        }

    polarities = []
    subjectivities = []

    for sentence in sentences:
        blob = TextBlob(sentence)
        polarities.append(blob.sentiment.polarity)
        subjectivities.append(blob.sentiment.subjectivity)

    avg_polarity = round(sum(polarities) / len(polarities), 4)
    avg_subjectivity = round(sum(subjectivities) / len(subjectivities), 4)

    return {
        "average_polarity": avg_polarity,
        "average_subjectivity": avg_subjectivity,
        "tone_arc": polarities  # this can be plotted or summarized further
    }


if __name__ == "__main__":
    sample_text = (
        "Entropy is strange. At first, it feels like a confusing topic. "
        "But the more you look at it, the more beautiful it becomes. "
        "Black holes, though, are terrifying. They break our understanding of time itself."
    )

    tone_profile = analyze_tone(sample_text)
    print("Avg Polarity:", tone_profile["average_polarity"])
    print("Tone Arc:", tone_profile["tone_arc"][:5])
