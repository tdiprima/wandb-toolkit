# Adapted from W&B Weave
import weave
import json
import os
from openai import OpenAI

@weave.op()  # 🐝 Decorator to track requests
def extract_fruit(sentence: str) -> dict:
    # Initialize OpenAI client with API key from environment variable
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    system_prompt = "Parse sentences into a JSON dict with keys: fruit, color, and flavor."
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": sentence}
        ],
        temperature=0.7,
        response_format={"type": "json_object"}
    )
    extracted = response.choices[0].message.content
    return json.loads(extracted)

# Initialize W&B Weave
weave.init('PyTorch Experiments')  # 🐝

# Test the function with a sample sentence
sentence = "There are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy."
result = extract_fruit(sentence)
print(result)
