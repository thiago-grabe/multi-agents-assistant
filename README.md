# PydanticAI Sales Q&A Agents with Self-Reflection

This repository demonstrates how to build sophisticated **Sales AI Agents** using [PydanticAI](https://github.com/pydantic-ai/pydantic-ai) and OpenAI's GPT models. The system features a two-agent collaboration architecture with detailed logging and self-correction capabilities for sales-related questions and scenarios.

> **🎯 Enhanced Agent Architecture**  
> This project showcases an advanced dual-agent system:
> 1. **Primary Sales Agent** – provides comprehensive sales answers with structured output and confidence scoring
> 2. **Reflection & Quality Agent** – reviews, validates, and improves responses with detailed analysis
> 3. **Comprehensive Logging** – tracks all agent decisions and processes step-by-step
> 4. **Rich Console Output** – beautiful formatted output for better debugging and monitoring

---

## 🌟 Key Features

- **🤖 Dual-Agent Architecture**: Primary sales agent + reflection agent for quality assurance
- **📊 Structured Outputs**: Type-safe responses with Pydantic validation
- **🔍 Detailed Logging**: Step-by-step process visualization with Rich console formatting
- **⚡ Real-time Feedback**: Confidence scoring and quality assessment
- **🎨 Beautiful UI**: Enhanced console output with colors, panels, and tables
- **🔧 Environment Management**: Secure API key handling with .env configuration
- **📋 Comprehensive Schemas**: Detailed response structures with metadata

---

## 📂 Repository Structure

```
pydanticai-sales-agents/
├── .env                              # Environment variables (created automatically)
├── .gitignore                        # Git ignore patterns
├── README.md                         # This comprehensive guide
├── requirements.txt                  # Python dependencies with versions
└── notebooks/
    └── me_agents_example.ipynb       # Enhanced sales agents notebook
```

### 📁 File Descriptions

- **`.env`** – Auto-generated environment configuration with OpenAI settings
- **`.gitignore`** – Protects sensitive files and caches
- **`README.md`** – Complete setup and usage documentation
- **`requirements.txt`** – All Python dependencies with version constraints
- **`notebooks/me_agents_example.ipynb`** – Interactive demonstration of the sales agent system

---

## 🔧 Installation & Setup

### 1. **Clone and Navigate**
```bash
git clone https://github.com/<your-username>/pydanticai-sales-agents.git
cd pydanticai-sales-agents
```

### 2. **Environment Setup**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate      # macOS/Linux
# venv\Scripts\activate       # Windows
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Configure API Keys**
The `.env` file is automatically created. Edit it to add your OpenAI API key:
```bash
# Edit the .env file:
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL_NAME=gpt-3.5-turbo
OPENAI_MODEL_TEMPERATURE=0.7
DEBUG_MODE=True
```

---

## 🚀 Usage Guide

### **Quick Start**
1. **Launch Jupyter Notebook**
   ```bash
   cd notebooks
   jupyter notebook me_agents_example.ipynb
   ```

2. **Follow the Interactive Guide**
   The notebook includes:
   - 📦 **Dependency Installation**: Automated setup with progress tracking
   - 🔧 **Environment Configuration**: API key validation and setup
   - 📋 **Schema Definition**: Structured output models with validation
   - 🤖 **Agent Creation**: Primary and reflection agents with detailed prompts
   - 💬 **Sales Scenarios**: Real-world sales questions and answers
   - 🔍 **Quality Analysis**: Reflection and improvement processes

### **Example Sales Scenarios**

The system handles various sales scenarios:

- **🎯 Sales Strategy**: "How do I handle price objections from enterprise clients?"
- **📞 Cold Calling**: "What's the best approach for cold calling in the SaaS industry?"
- **🤝 Relationship Building**: "How can I build long-term relationships with B2B customers?"
- **📊 Performance Metrics**: "What KPIs should I track for sales effectiveness?"
- **🏆 Closing Techniques**: "Walk me through advanced closing techniques for high-value deals"

---

## 📚 Technical Architecture

### **Agent Schemas**

#### `SalesAnswer` - Primary Response Schema
```python
class SalesAnswer(BaseModel):
    answer: str                    # Comprehensive sales response
    confidence_score: float        # AI confidence (0.0-1.0)
    key_points: List[str]         # Actionable takeaways
    sales_category: str           # Topic classification
```

#### `ReflectionAnalysis` - Quality Assessment Schema
```python
class ReflectionAnalysis(BaseModel):
    reviewed_answer: str              # Improved response
    quality_score: float              # Quality assessment (0.0-1.0)
    improvements_made: List[str]      # Specific enhancements
    missing_elements: List[str]       # Identified gaps
    additional_considerations: str    # Extra insights
```

### **Agent Configuration**

#### Primary Sales Agent
- **Model**: GPT-3.5-turbo (configurable)
- **Role**: Sales expert with comprehensive knowledge
- **Output**: Structured `SalesAnswer` with metadata
- **Features**: Confidence scoring, categorization, key points extraction

#### Reflection Agent
- **Model**: GPT-3.5-turbo (configurable)
- **Role**: Quality assurance and improvement specialist
- **Output**: Detailed `ReflectionAnalysis` with enhancements
- **Features**: Quality scoring, gap analysis, improvement suggestions

### **Enhanced Features**

- **🎨 Rich Console Output**: Beautiful formatted output with colors and panels
- **📊 Progress Tracking**: Step-by-step process visualization
- **🔍 Debug Logging**: Comprehensive logging for troubleshooting
- **⚡ Real-time Validation**: Immediate schema validation and error handling
- **🔧 Environment Management**: Secure configuration with validation

---

## 🛠 Dependencies Explained

### **Core Framework**
- **`pydantic-ai>=0.3.0`** – Advanced AI agent framework with type safety
- **`openai>=1.0.0`** – Official OpenAI API client with latest features

### **Environment & Configuration**
- **`python-dotenv>=1.0.0`** – Secure environment variable management
- **`rich>=13.0.0`** – Beautiful console output with colors and formatting

### **Development Environment**
- **`jupyter>=1.0.0`** – Interactive notebook environment
- **`ipykernel>=6.0.0`** – Jupyter kernel for Python execution

---

## 🎯 Advanced Usage

### **Custom Sales Scenarios**
Modify the notebook to handle specific sales scenarios:

```python
# Custom sales question
question = "How do I negotiate with procurement teams in enterprise sales?"

# Run through both agents
primary_result = sales_agent.run_sync(question)
reflection_result = reflection_agent.run_sync(
    f"Question: {question}\nAnswer: {primary_result.output.answer}"
)
```

### **Configuration Options**
Customize agent behavior through environment variables:

```bash
# .env configuration
OPENAI_MODEL_NAME=gpt-4                    # Use GPT-4 for enhanced responses
OPENAI_MODEL_TEMPERATURE=0.3               # Lower temperature for more focused answers
DEBUG_MODE=True                            # Enable detailed logging
```

---

## 🔍 Monitoring & Debugging

The system provides comprehensive monitoring:

- **🎯 Agent Decision Tracking**: See how each agent processes questions
- **📊 Confidence Metrics**: Monitor AI confidence levels
- **🔍 Quality Assessments**: Track improvement suggestions
- **⚡ Performance Logging**: Execution time and resource usage
- **🛠 Error Handling**: Detailed error messages with suggestions

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the Repository**
   ```bash
   git fork https://github.com/<your-username>/pydanticai-sales-agents.git
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/new-sales-scenario
   ```

3. **Make Changes**
   - Add new sales scenarios
   - Enhance agent prompts
   - Improve output formatting
   - Add new validation schemas

4. **Submit Pull Request**
   ```bash
   git commit -am "Add enterprise sales scenarios"
   git push origin feature/new-sales-scenario
   ```

### **Contribution Ideas**
- 🎯 New sales scenarios and use cases
- 📊 Enhanced metrics and scoring systems
- 🔧 Additional agent configurations
- 📚 Documentation improvements
- 🧪 Test cases and validation

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **PydanticAI Team** – For the excellent AI agent framework
- **OpenAI** – For providing powerful language models
- **Rich Library** – For beautiful console formatting
- **Sales Community** – For inspiring real-world scenarios and use cases

---

## 📞 Support

Need help? Here are your options:

- 📖 **Documentation**: Check the notebook for detailed examples
- 🐛 **Issues**: Report bugs via GitHub Issues
- 💬 **Discussions**: Join the conversation in GitHub Discussions
- 📧 **Contact**: Reach out for custom implementations

---

**⭐ Star this repo if you find it helpful!**
