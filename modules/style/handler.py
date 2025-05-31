import json
import os
from typing import List, Dict

from modules.style.sentence_stats import compute_sentence_stats
from modules.style.tone_analyzer import analyze_tone
from modules.style.structure_detector import detect_structure_patterns
from modules.style.phrase_extractor import extract_common_phrases, extract_cta_phrases

class StyleProfileBuilder:
    def __init__(self):
        pass  # placeholder for config if needed later

    def build_profile(self, transcript_text: str) -> Dict:
        stats = compute_sentence_stats(transcript_text)
        tone = analyze_tone(transcript_text)
        structure = detect_structure_patterns(transcript_text)
        phrases = extract_common_phrases(transcript_text)
        ctas = extract_cta_phrases(transcript_text)

        profile = {
            "average_sentence_length": stats["avg_sentence_length"],
            "vocabulary_diversity": stats["vocab_diversity"],
            "average_polarity": tone["average_polarity"],
            "average_subjectivity": tone["average_subjectivity"],
            "tone_arc": tone["tone_arc"],
            "structure": structure,
            "common_phrases": {
                "bigrams": phrases["common_bigrams"],
                "trigrams": phrases["common_trigrams"]
            },
            "call_to_actions": ctas
        }

        return profile

    def save_profile(self, profile: Dict, out_path: str):
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(profile, f, indent=2)

if __name__ == "__main__":
    builder = StyleProfileBuilder()

    with open("/Users/ranjana/Documents/codes/personal_workspace/Scriptive/data/processed/transcripts/ZC98ZK6Ivug.txt", "r") as f:
        full_text = f.read()

    profile = builder.build_profile(full_text)
    builder.save_profile(profile, "/Users/ranjana/Documents/codes/personal_workspace/Scriptive/data/processed/style_profiles/ZC98ZK6Ivug.json")

    print("Style profile saved.")
