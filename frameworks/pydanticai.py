# Install: pip install pydantic-ai openai
from pydantic_ai import Agent

# Create an agent with OpenAI GPT-3.5 and a sales assistant persona
agent = Agent(
    "openai:gpt-3.5-turbo",  # OpenAI model to use
    system_prompt="You are a friendly sales assistant."  # System instructions
)

# Run the agent synchronously with a customer question
result = agent.run_sync("Do you have any current promotions on laptops?")
print(result.output)