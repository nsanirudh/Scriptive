import re
from nltk.tokenize import sent_tokenize
from typing import Dict

def detect_structure_patterns(text: str) -> Dict:
    sentences = sent_tokenize(text)
    total = len(sentences)
    if total < 10:
        return {"intro": "", "body": "", "outro": ""}

    # Define intro/body/outro splits
    intro_end = max(2, int(0.1 * total))
    outro_start = max(int(0.9 * total), total - 3)

    intro = sentences[:intro_end]
    body = sentences[intro_end:outro_start]
    outro = sentences[outro_start:]

    return {
        "intro": classify_intro(intro),
        "body": classify_body(body),
        "outro": classify_outro(outro)
    }

def classify_intro(intro_sentences) -> str:
    joined = " ".join(intro_sentences).lower()
    if re.search(r"\?", joined):
        return "starts with a question"
    if re.search(r"(imagine|what if|have you ever)", joined):
        return "uses curiosity or thought experiment"
    if re.search(r"(in this video|today we're going to)", joined):
        return "declarative setup"
    return "no clear pattern"

def classify_body(body_sentences) -> str:
    joined = " ".join(body_sentences).lower()
    if re.search(r"(for example|let's take|consider)", joined):
        return "uses illustrative examples"
    if re.search(r"(step|first|next|then)", joined):
        return "stepwise explanation"
    if re.search(r"(analogy|like|as if)", joined):
        return "uses analogies"
    return "neutral or mixed style"

def classify_outro(outro_sentences) -> str:
    joined = " ".join(outro_sentences).lower()
    if re.search(r"(subscribe|like|comment)", joined):
        return "ends with call-to-action"
    if re.search(r"(stay curious|until next time|that’s all)", joined):
        return "has signature sign-off"
    if re.search(r"\?", joined):
        return "ends with an open-ended question"
    return "neutral close"

if __name__ == "__main__":
    sample = """
    What if I told you the universe is slowly dying? Entropy is a measure of disorder.
    Let's explore how it governs everything. For example, your coffee cooling down...
    Subscribe for more science. And as always, stay curious!
    """
    result = detect_structure_patterns(sample)
    print(result)
