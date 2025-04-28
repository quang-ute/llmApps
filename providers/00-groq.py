import os
from groq import Groq
from rich import print
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)
completion = client.chat.completions.create(
    model = "llama3-70b-8192",
    messages = [
    {
        "role":"system",
        "content":"You are a helful AI assistant."
    },
    {
        "role":"user",
        "content":"""
            What is langchain.
            """
    },
    ],
    temperature = 0.7,
)
#print(completion)

print(completion.choices[0].message.content)
