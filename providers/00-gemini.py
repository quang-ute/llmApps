import os
import google.generativeai as genai
from rich import print
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-pro")

chat = model.start_chat(
    history = [
        {
            "role":"user",
            "parts":"You are a helpful AI assistant."
        }
    ]
)
# Send the user query
response = chat.send_message(
    content="What is LangChain?",
    generation_config={"temperature": 0.7}
)

# Print the response
print(response.text)