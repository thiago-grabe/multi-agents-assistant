# PydanticAI Agents with Multiple Frameworks

This repository demonstrates how to build AI agents using different frameworks including [PydanticAI](https://github.com/pydantic-ai/pydantic-ai), [LangGraph](https://github.com/langchain-ai/langgraph), and [CrewAI](https://github.com/joaomdmoura/crewAI). The project showcases various approaches to creating conversational AI agents with proper environment management and structured outputs.

> **🎯 Multi-Framework Approach**  
> This project demonstrates different AI agent frameworks:
> 1. **PydanticAI** – Type-safe AI agents with structured outputs
> 2. **LangGraph** – Graph-based agent workflows with React agents
> 3. **CrewAI** – Multi-agent collaboration framework
> 4. **Environment Management** – Secure API key handling with .env configuration

---

## 🌟 Key Features

- **🤖 Multiple Frameworks**: PydanticAI, LangGraph, and CrewAI examples
- **📊 Structured Outputs**: Type-safe responses with Pydantic validation
- **🔧 Environment Management**: Secure API key handling with .env configuration
- **📋 Comprehensive Examples**: Working examples for each framework
- **🔍 Error Handling**: Proper validation and error messages
- **📚 Jupyter Notebooks**: Interactive examples with detailed explanations

---

## 📂 Repository Structure

```
pydanticai-me-agents/
├── .env                              # Environment variables (API keys)
├── .gitignore                        # Git ignore patterns
├── README.md                         # This comprehensive guide
├── requirements.txt                  # Python dependencies with versions
├── frameworks/                       # Framework-specific examples
│   ├── pydanticai.py                # PydanticAI sales agent example
│   ├── langgraph_example.py         # LangGraph React agent example
│   ├── crewai_example.py            # CrewAI multi-agent example
│   └── requirements-frameworks.txt   # Framework-specific dependencies
└── notebooks/                        # Interactive examples
    └── reflection_sales_agent.ipynb  # Enhanced sales agents notebook
```

### 📁 File Descriptions

- **`.env`** – Environment configuration with OpenAI API key
- **`.gitignore`** – Protects sensitive files and caches
- **`README.md`** – Complete setup and usage documentation
- **`requirements.txt`** – All Python dependencies with version constraints
- **`frameworks/`** – Framework-specific examples and requirements
- **`notebooks/`** – Interactive Jupyter notebook examples

---

## 🔧 Installation & Setup

### 1. **Clone and Navigate**
```bash
git clone https://github.com/<your-username>/pydanticai-me-agents.git
cd pydanticai-me-agents
```

### 2. **Environment Setup**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows
```

### 3. **Install Dependencies**
```bash
# Install main dependencies
pip install -r requirements.txt

# Install framework-specific dependencies
pip install -r frameworks/requirements-frameworks.txt
```

### 4. **Configure API Keys**
Copy the example environment file and add your OpenAI API key:
```bash
# Copy the example file
cp .env-example .env

# Edit the .env file with your API key:
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL_NAME=gpt-3.5-turbo
OPENAI_MODEL_TEMPERATURE=0.7
DEBUG_MODE=True
```

---

## 🚀 Usage Guide

### **Quick Start Examples**

#### 1. **PydanticAI Agent**
```bash
python frameworks/pydanticai.py
```
Creates a sales assistant agent with structured outputs and confidence scoring.

#### 2. **LangGraph Agent**
```bash
python frameworks/langgraph_example.py
```
Demonstrates a React agent using LangGraph for conversational AI.

#### 3. **CrewAI Multi-Agent System**
```bash
python frameworks/crewai_example.py
```
Shows multi-agent collaboration for complex tasks.

### **Interactive Notebook**
```bash
cd notebooks
jupyter notebook reflection_sales_agent.ipynb
```

---

## 📚 Framework Examples

### **PydanticAI Example** (`frameworks/pydanticai.py`)
```python
from pydantic_ai import Agent

# Create a sales assistant agent
agent = Agent(
    "openai:gpt-3.5-turbo",
    system_prompt="You are a friendly sales assistant."
)

# Run the agent
result = agent.run_sync("Do you have any current promotions on laptops?")
print(result.output)
```

**Features:**
- Type-safe agent creation
- Structured outputs with Pydantic validation
- Simple and clean API
- Built-in error handling

### **LangGraph Example** (`frameworks/langgraph_example.py`)
```python
from langgraph.prebuilt import create_react_agent

# Create a React agent
agent = create_react_agent(
    model="openai:gpt-3.5-turbo",
    tools=[],
    prompt="You are a helpful sales assistant"
)

# Query the agent
response = agent.invoke({
    "messages": [{"role": "user", "content": "What is your return policy?"}]
})
```

**Features:**
- Graph-based agent workflows
- React agent pattern
- Tool integration capabilities
- Message-based interaction

### **CrewAI Example** (`frameworks/crewai_example.py`)
```python
from crewai import Agent, Task, Crew

# Create specialized agents
researcher = Agent(
    role='Research Analyst',
    goal='Find accurate information about sales strategies',
    backstory='Expert in market research and data analysis'
)

# Create tasks and crew
task = Task(description='Research best sales practices')
crew = Crew(agents=[researcher], tasks=[task])
result = crew.kickoff()
```

**Features:**
- Multi-agent collaboration
- Role-based agent design
- Task delegation
- Complex workflow management

---

## 🛠 Dependencies

### **Core Dependencies** (`requirements.txt`)
```
pydantic-ai==0.3.2
python-dotenv==1.1.0
openai==1.90.0
rich==14.0.0
ipykernel==6.29.5
langgraph==0.4.8
langchain-openai==0.3.24
langchain==0.3.26
langchain-core==0.3.66
langchain-text-splitters==0.3.8
crewai==0.130.0
```

### **Framework-Specific Dependencies** (`frameworks/requirements-frameworks.txt`)
```
langgraph==0.4.8
langchain-openai==0.3.24
langchain==0.3.26
langchain-core==0.3.66
langchain-text-splitters==0.3.8
crewai==0.130.0
pydantic-ai==0.3.2
openai==1.90.0
python-dotenv==1.1.0
```

---

## 🔍 Environment Configuration

### **Required Environment Variables**
```bash
# .env file structure
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL_NAME=gpt-3.5-turbo
OPENAI_MODEL_TEMPERATURE=0.7
DEBUG_MODE=True
```

### **API Key Setup**
1. Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Copy `.env-example` to `.env`
3. Add your API key to the `.env` file
4. All examples will automatically load the environment variables

---

## 🎯 Advanced Usage

### **Custom Agent Creation**
Each framework supports customization:

```python
# PydanticAI with custom schema
from pydantic import BaseModel

class CustomResponse(BaseModel):
    answer: str
    confidence: float
    metadata: dict

agent = Agent("openai:gpt-4", response_model=CustomResponse)
```

### **Environment Management**
All examples include proper environment handling:
```python
import os
from dotenv import load_dotenv

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in environment variables.")
```

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the Repository**
2. **Create Feature Branch**
   ```bash
   git checkout -b feature/new-framework-example
   ```
3. **Add New Examples**
   - Create new framework examples
   - Update requirements files
   - Add documentation
4. **Submit Pull Request**

### **Contribution Ideas**
- 🎯 New framework examples (AutoGen, Semantic Kernel, etc.)
- 📊 Enhanced agent configurations
- 🔧 Additional tool integrations
- 📚 Documentation improvements
- 🧪 Test cases and validation

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- **PydanticAI Team** – For the excellent AI agent framework
- **LangGraph Team** – For graph-based agent workflows
- **CrewAI Team** – For multi-agent collaboration framework
- **OpenAI** – For providing powerful language models

---

## 📞 Support

Need help? Here are your options:

- 📖 **Documentation**: Check the examples in the `frameworks/` directory
- 🐛 **Issues**: Report bugs via GitHub Issues
- 💬 **Discussions**: Join the conversation in GitHub Discussions

---

**⭐ Star this repo if you find it helpful!**
