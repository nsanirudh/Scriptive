import os
import openai
from datetime import datetime
from pathlib import Path
from typing import Optional

# Ensure you are using openai>=1.0.0
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ScriptGenerator:
    def __init__(
        self,
        model: str = "gpt-4",
        temperature: float = 0.7,
        max_tokens: int = 1500,
        log_dir: str = "data/processed/prediction_logs"
    ):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def generate_script(self, prompt: str, topic: str = "untitled") -> str:
        try:
            response = client.chat.completions.create(
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                messages=[
                    {"role": "system", "content": "You are an expert YouTube script writer."},
                    {"role": "user", "content": prompt}
                ]
            )
            output = response.choices[0].message.content.strip()
            self._save_log(prompt, output, topic)
            return output
        except Exception as e:
            print(f"[ERROR] LLM generation failed: {e}")
            return "[ERROR] Generation failed."

    def _save_log(self, prompt: str, output: str, topic: str):
        safe_topic = topic.lower().replace(" ", "-")[:40]
        timestamp = datetime.now().isoformat(timespec="seconds").replace(":", "-")
        filename = f"{timestamp}_{safe_topic}.md"
        path = Path(self.log_dir) / filename

        content = f"""
# Topic: {topic}
**Model**: {self.model}  
**Temperature**: {self.temperature}  
**Max Tokens**: {self.max_tokens}  
**Timestamp**: {timestamp}  

---

## Prompt

{prompt}

---

## Generated Script

{output}
"""

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[LOG] Prompt and output saved to {path}")


if __name__ == "__main__":
    from modules.prediction.prompt_builder import build_generation_prompt
    import json

    style = json.load(open("data/processed/style_profiles/veritasium.json"))
    context_chunks = [{"text": "Entropy increases over time..."}, {"text": "Black holes are high entropy objects..."}]

    prompt = build_generation_prompt(
        topic="Entropy in Black Holes",
        style_profile=style,
        context_chunks=context_chunks,
        tone="dramatic",
        audience="physics undergrads",
        length="medium"
    )

    gen = ScriptGenerator()
    result = gen.generate_script(prompt, topic="Entropy in Black Holes")
    print(result)
