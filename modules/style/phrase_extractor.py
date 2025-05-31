import re
from typing import List, Dict
from collections import Counter
from nltk.util import ngrams
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

STOPWORDS = set(stopwords.words("english"))

def extract_common_phrases(text: str, top_k: int = 10) -> Dict[str, List[str]]:
    sentences = sent_tokenize(text.lower())
    all_tokens = [word_tokenize(sent) for sent in sentences]

    bigram_freq = Counter()
    trigram_freq = Counter()

    for tokens in all_tokens:
        tokens_clean = [t for t in tokens if t.isalpha() and t not in STOPWORDS]
        bigrams = ngrams(tokens_clean, 2)
        trigrams = ngrams(tokens_clean, 3)
        bigram_freq.update(bigrams)
        trigram_freq.update(trigrams)

    common_bigrams = [" ".join(p) for p, _ in bigram_freq.most_common(top_k)]
    common_trigrams = [" ".join(p) for p, _ in trigram_freq.most_common(top_k)]

    return {
        "common_bigrams": common_bigrams,
        "common_trigrams": common_trigrams
    }

def extract_cta_phrases(text: str) -> List[str]:
    patterns = [
        r"(subscribe( to my channel)?)",
        r"(don’t forget to (like|subscribe|comment))",
        r"(smash that like button)",
        r"(see you (next time|soon|in the next video))",
        r"(stay curious|keep learning|that’s all folks)",
    ]

    matches = []
    for pattern in patterns:
        found = re.findall(pattern, text.lower())
        matches.extend([" ".join(f) if isinstance(f, tuple) else f for f in found])

    return list(set(matches))

if __name__ == "__main__":
    sample = """
    What if time isn’t real? That’s the idea we’ll explore today.
    Don’t forget to subscribe to my channel and smash that like button.
    Stay curious — see you next time!
    """

    phrases = extract_common_phrases(sample)
    ctas = extract_cta_phrases(sample)

    print("Bigrams:", phrases["common_bigrams"])
    print("Trigrams:", phrases["common_trigrams"])
    print("CTAs:", ctas)
