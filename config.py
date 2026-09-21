import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq").strip().lower()

if PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

else:
    raise SystemExit("Use PROVIDER=groq in your .env file.")

if not API_KEY:
    raise SystemExit("No Groq API key found in .env")

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)


# Private student data
STUDENT_MARKS = {
    "Lokesh": 85,
    "Arun": 72,
    "Kavin": 91
}


QUESTIONS = [
    "What is Lokesh's mark?",
    "Who scored the highest mark?",
    "What is the average mark of Lokesh and Arun?",
    "Write a two-line welcome message for students."
]


def banner(system_name):
    print(
        f"\n=== {system_name} | "
        f"provider: {PROVIDER} | model: {MODEL} ===\n"
    )