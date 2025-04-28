from dotenv import load_dotenv
from litellm import completion
import os
from rich import print

load_dotenv()

api_key = os.environ["GEMINI_API_KEY"]

def get_llm_response(message):
    response = completion(
        #model = "groq/llama3-70b-8192",
        #model = "deepseek/deepseek-chat",
        model ="gemini/gemini-2.5-flash-preview-04-17",
        messages=message,
        stream=False
    )
    return response

messages = [
    {
        "role":"system",
        "content":"You are a helpful AI assistant"
    },
    {
        "role":"user",
        "content":"Why is AC more popular than DC?"
    }
]


response = get_llm_response(messages)
#print(response)
print(response.choices[0].message.content)