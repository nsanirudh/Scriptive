from typing import List, Dict

def build_generation_prompt(
    topic: str,
    style_profile: Dict,
    context_chunks: List[Dict],
    audience: str = "general audience",
    tone: str = "educational",
    length: str = "medium"
) -> str:
    """
    Assembles a prompt for the LLM using topic, context, and style profile.
    """
    # Use top context passages
    context_text = "\n\n".join(f"Context {i+1}: {chunk['text']}" for i, chunk in enumerate(context_chunks))

    # Extract style cues
    hook_pattern = style_profile.get("structure", {}).get("intro", "")
    outro_pattern = style_profile.get("structure", {}).get("outro", "")
    avg_len = style_profile.get("average_sentence_length", 14)
    tone_hint = style_profile.get("average_polarity", 0.1)

    signature_phrases = ", ".join(style_profile.get("call_to_actions", [])[:3])
    common_phrases = ", ".join(style_profile.get("common_phrases", {}).get("bigrams", [])[:5])

    # Construct prompt
    prompt = f"""
    You are a creative scriptwriter for an educational YouTube channel.
    
    ## TASK:
    Write a script on the topic: **{topic}**
    
    ## OUTPUT REQUIREMENTS:
    - Length: {length}
    - Tone: {tone}
    - Audience: {audience}
    - Style: Match the following creator's style
    
    ## STYLE PROFILE:
    - Intro Style: {hook_pattern}
    - Outro Style: {outro_pattern}
    - Sentence Length: Around {avg_len} words
    - Signature Phrases: {signature_phrases}
    - Common Expressions: {common_phrases}
    - Tone indicator (polarity): {tone_hint}
    
    ## CONTEXT:
    Use the following reference chunks as factual support. Paraphrase or reframe as needed.
    
    {context_text}
    
    ## FORMAT:
    Return the script in 4 parts:
    1. Hook
    2. Main Body
    3. Analogy / Story Element
    4. Outro / CTA
"""
    return prompt.strip()


if __name__ == "__main__":
    import json
    from pathlib import Path

    style = json.loads(Path("data/processed/style_profiles/veritasium.json").read_text())
    chunks = [
        {"text": "Entropy is a measure of disorder..."},
        {"text": "Black holes challenge our understanding of time..."}
    ]

    prompt = build_generation_prompt(
        topic="Entropy in Black Holes",
        style_profile=style,
        context_chunks=chunks,
        audience="college science students",
        tone="dramatic",
        length="long"
    )

    print(prompt)
