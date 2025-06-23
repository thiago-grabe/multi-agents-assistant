# Install: pip install crewai openai
from crewai import Crew, Agent, Task

# Define a sales assistant agent with a role and goal
assistant = Agent(
    role="Sales Assistant",
    goal="Help customers with sales-related questions in a friendly tone",
    backstory="Experienced in retail and customer service"
)

# Define a task for the agent (what it should do)
sales_task = Task(
    description="Answer the customer's question helpfully",
    agent=assistant,
    expected_output="A helpful, accurate answer"
)

# Create a Crew with the single agent and task
crew = Crew(agents=[assistant], tasks=[sales_task])

# Run the crew with a user query (the 'question' can be passed via inputs if used in templates)
result = crew.kickoff(inputs={"question": "Do you offer discounts on bulk orders?"})
print(result)