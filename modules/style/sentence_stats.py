import re
from typing import List, Dict
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize



def compute_sentence_stats(text: str) -> Dict:
    sentences = sent_tokenize(text)
    if not sentences:
        return {"avg_sentence_length": 0, "vocab_diversity": 0}

    words = word_tokenize(text.lower())
    vocab = set(words)

    return {
        "avg_sentence_length": round(sum(len(word_tokenize(s)) for s in sentences) / len(sentences), 2),
        "vocab_diversity": round(len(vocab) / len(words), 4)
    }

if __name__ == "__main__":
    transcript = "In 1982, there was one SAT question that every single student got wrong. Here it is in the figure above. The radius of circle A is one third the radius of circle B. Starting from the position shown in the figure, circle A rolls around circle B. At the end of how many revolutions of circle A will the center of the circle first reach its starting point? Is it A3 halves, B3 C6 D9 halves or E9? This exam gave students 30 minutes to solve 25 problems, so about a minute each. So feel free to pause the video here and try to solve it. What is your answer? I'll tell you right now that option B or 3 is not correct. When I first saw this problem, my intuitive answer was B because the circumference of a circle is just 2 PI r, and since the radius of circle B is three times the radius of circle A, the circumference of circle B must also be three times the circumference of circle A. So logically, it should take three full rotations of circle A to roll around circle B. So my answer is was three. This is wrong. But so are answers A, C, D, and E. The reason no one got question 17 correct is that the test writers themselves got it wrong. They also thought the answer was three."
    stats = compute_sentence_stats(transcript)
    print(stats)
