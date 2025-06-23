# Install: pip install langgraph langchain-openai python-dotenv
import os
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent

# Load environment variables from .env file
load_dotenv()

# Check if OpenAI API key is available
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please check your .env file.")

# Create a sales assistant agent with OpenAI GPT-3.5
agent = create_react_agent(
    model="openai:gpt-3.5-turbo",              # LLM model (OpenAI GPT-3.5)
    tools=[],                                  # No external tools for simplicity
    prompt="You are a helpful sales assistant" # System prompt for the agent
)

# Query the agent with a user question
response = agent.invoke({
    "messages": [{"role": "user", "content": "What is your return policy?"}]
})
print(response)