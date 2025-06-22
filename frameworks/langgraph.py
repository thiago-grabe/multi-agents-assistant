# Install: pip install langgraph langchain-openai
from langgraph.prebuilt import create_react_agent

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