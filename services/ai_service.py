import json
import urllib.request
import urllib.error

OLLAMA_URL = "http://172.28.224.1:11434/api/generate"
MODEL_NAME = "qwen2.5:3b"


def generate_ai_response(question, hardware_info):

    prompt = f"""
You are a Linux Hardware Assistant.

Here is the user's hardware information:

{hardware_info}

User Question:
{question}

Answer based only on the available hardware information.
If information is unavailable, say so.
"""

    data = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    request = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))

        return result["response"]

    except urllib.error.URLError as error:
        return f"Ollama connection error: {error}"