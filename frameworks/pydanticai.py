# Install: pip install pydantic-ai openai python-dotenv
import os
from dotenv import load_dotenv
from pydantic_ai import Agent

# Load environment variables from .env file
load_dotenv()

# Check if OpenAI API key is available
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please check your .env file.")

# Create an agent with OpenAI GPT-3.5 and a sales assistant persona
agent = Agent(
    "openai:gpt-3.5-turbo",  # OpenAI model to use
    system_prompt="You are a friendly sales assistant."  # System instructions
)

# Run the agent synchronously with a customer question
result = agent.run_sync("Do you have any current promotions on laptops?")
print(result.output)