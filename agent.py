import json

from config import client, MODEL, QUESTIONS, banner
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = (
    "You are a student marks assistant. "
    "Never guess a student's mark. "
    "Use get_mark when you need a student's mark. "
    "Use calculator for arithmetic. "
    "Students available are Lokesh, Arun and Kavin."
)


def agent(question, max_steps=5):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(1, max_steps + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return message.content.strip()

        messages.append({
            "role": "assistant",
            "content": message.content or "",
            "tool_calls": [
                {
                    "id": call.id,
                    "type": "function",
                    "function": {
                        "name": call.function.name,
                        "arguments": call.function.arguments
                    }
                }
                for call in message.tool_calls
            ]
        })

        for call in message.tool_calls:

            name = call.function.name

            arguments = json.loads(
                call.function.arguments or "{}"
            )

            function = TOOL_FUNCTIONS.get(name)

            result = function(**arguments)

            print(
                f"   step {step}: "
                f"{name}({arguments}) -> {result}"
            )

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result
            })

    return "Maximum steps reached."


if __name__ == "__main__":

    banner("SYSTEM 3: AI AGENT")

    for question in QUESTIONS:

        print("Q:", question)
        print("A:", agent(question))
        print("-" * 70)