import os
#from openai import OpenAI
from groq import Groq
from rich import print
from dotenv import load_dotenv


# Remember to load the environment variables. You should have the Groq API Key in there :)
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
#api_key = os.getenv("GEMINI_API_KEY")
client = Groq()

# First prompt
generation_chat_history = [
    {
        "role": "system",
        "content": 
        """
            You are a 10-year experience programmer tasked with generating high-quality python code.
            Your task is to Generate the best content possible for the user's request. 
            If the user provides critique, respond with a revised version of your previous attempt.
                    """
    },
    {   "role": "user",
        "content": 
        """
        Generate a python implementation of quicksort algorithm. 
        """
    }
]
# client = OpenAI(
#     api_key=api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# py_code = client.chat.completions.create(
#     model ="gemini-2.5-flash-preview-04-17",
#     messages=generation_chat_history,
# ).choices[0].message.content
# First generation
py_code = client.chat.completions.create(
    messages=generation_chat_history,
    model="llama3-70b-8192"
).choices[0].message.content

generation_chat_history.append(
    {
        "role": "assistant",
        "content": py_code
    }
)
print(py_code)

