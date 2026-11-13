import os
import json
import urllib.request
import urllib.error

from services.tool_executor import execute_tool

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama-3.3-70b-versatile"

ALLOWED_TOOLS = ["cpu", "memory", "storage", "gpu"]

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": name,
            "description": f"Get {name} hardware information",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
    for name in ALLOWED_TOOLS
]


def call_groq(messages):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY is missing")

    data = {
        "model": MODEL_NAME,
        "messages": messages,
        "tools": TOOLS,
        "tool_choice": "auto"
    }

    request = urllib.request.Request(
        GROQ_URL,
        data=json.dumps(data).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        method="POST"
    )

    with urllib.request.urlopen(request, timeout=120) as response:
        return json.loads(response.read().decode("utf-8"))


def generate_ai_response(question, hardware_info=None):
    messages = [
        {
            "role": "system",
            "content": """
            You are a Linux Hardware Assistant.
            Use hardware tools when hardware information is needed.
            Never guess hardware specifications.
            If information is unavailable, say so.
            """
        },
        {
            "role": "user",
            "content": question
        }
    ]

    try:
        for _ in range(4):
            result = call_groq(messages)
            assistant_message = result["choices"][0]["message"]

            tool_calls = assistant_message.get("tool_calls")

            if not tool_calls:
                return assistant_message.get("content", "No answer generated.")

            messages.append(assistant_message)

            for tool_call in tool_calls:
                tool_name = tool_call["function"]["name"]
                tool_id = tool_call["id"]

                if tool_name in ALLOWED_TOOLS:
                    tool_result = execute_tool(tool_name)
                else:
                    tool_result = {"error": "Tool not allowed"}

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_id,
                    "content": json.dumps(tool_result)
                })

        return "Maximum tool calls reached."

    except urllib.error.HTTPError as error:
        details = error.read().decode("utf-8")
        return f"Groq API error: {details}"

    except (urllib.error.URLError, ValueError, KeyError) as error:
        return f"AI error: {error}"
