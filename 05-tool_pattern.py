from dotenv import load_dotenv
#from langchain_litellm import ChatLiteLLM
from langchain_google_genai import ChatGoogleGenerativeAI
#from litellm import completion
#from openai import OpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import BaseTool
import datetime
import random

import os

load_dotenv()

# api_key = os.environ["DEEPSEEK_API_KEY"]

# llm = ChatLiteLLM(
#     model="deepseek/deepseek-chat",
#     api_key=api_key,
#     api_base="https://api.deepseek.com/v1",
#     temperature=0,
# )
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# Initialize LLM with Google Gemini
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  # or "gemini-1.5-pro" depending on your access
        google_api_key=api_key,
        temperature=0,
    )
except Exception as e:
    print(f"Error initializing LLM: {e}")
    raise

# Define the Google Calendar tool
class GoogleCalendarTool(BaseTool):
    name: str = "Google Calendar"
    description: str = "Fetches information about your upcoming meetings and events from Google Calendar. Use this tool to check your schedule."
    
    def _run(self, query: str) -> str:

        now = datetime.datetime.now()       
        mock_meetings = [
            {
                "title": "Client Presentation",
                "time": "10:00 AM",
                "date": (now + datetime.timedelta(days=5)).strftime("%A, %B %d"),
                "attendees": "Client team, sales"
            }
        ]
        next_meeting = mock_meetings[0]
        return f"Your next meeting is '{next_meeting['title']}' at {next_meeting['time']} on {next_meeting['date']} with {next_meeting['attendees']}."

# Define the Weather tool
class GetWeatherTool(BaseTool):
    name: str = "Get Weather"
    description: str = "Gets the weather forecast for a specific time and location. Input should be 'location, date, time'"
    
    def _run(self, query: str) -> str:
        try:
            # Parse the input
            parts = [part.strip() for part in query.split(',')]
            location_data=["Paris, France","New York, USA","Tokyo, Japan"]
            # Check if location is in the predefined list
            
            # Handle different input formats
            if len(parts) == 3:
                location, date, time = parts
            elif len(parts) == 2:
                location, time = parts
                date = "today"
            elif len(parts) == 1:
                location = parts[0]
                date = "today"
                time = "now"
            else:
                return "Please provide location and optionally date and time."
            # Mock location 
            location= random.choice(location_data)
            # Mock weather data
            weather_conditions = ["Sunny", "Partly Cloudy", "Cloudy", "Light Rain", "Heavy Rain", "Thunderstorms", "Windy"]
            temperatures = range(15, 35)  # Celsius
            
            # Simulate weather based on input (for demo purposes this is random)
            condition = random.choice(weather_conditions)
            temperature = random.choice(temperatures)
            humidity = random.randint(30, 90)
            wind_speed = random.randint(0, 30)
            
            return f"Weather forecast for {location} on {date} at {time}: {condition}, {temperature}°C, Humidity: {humidity}%, Wind: {wind_speed} km/h"
            
        except Exception as e:
            return f"Error getting weather: {str(e)}"

# Create instances of the tools
tools = [GoogleCalendarTool(), GetWeatherTool()]


# Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run the agent with a sample query
response = agent.invoke("When is my next meeting? How is the weather at that time?")
print(response)