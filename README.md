# Research Agent

An intelligent AI-powered research assistant that leverages LangChain and Claude 3.5 Sonnet to conduct comprehensive research on any topic. The agent autonomously searches the web, queries Wikipedia, and generates structured research outputs with proper citations and source tracking.

## 🚀 Features

- **Multi-Source Research**: Combines web search (DuckDuckGo) and Wikipedia for comprehensive information gathering
- **Structured Output**: Returns research findings in a standardized format with topic, summary, sources, and tools used
- **Automated File Saving**: Saves research outputs to timestamped files for easy reference
- **Interactive Interface**: Simple command-line interface for research queries
- **AI-Powered Analysis**: Uses Claude 3.5 Sonnet for intelligent synthesis and analysis of gathered information
- **Tool Orchestration**: Intelligently selects and combines multiple research tools based on query requirements

## 🏗️ Architecture

The research agent is built using a modular architecture:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Main Script   │───▶│   LangChain      │───▶│   Claude 3.5    │
│   (main.py)     │    │   Agent          │    │   Sonnet        │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │
         ▼                       ▼
┌─────────────────┐    ┌──────────────────┐
│   Research      │    │   Tool Suite     │
│   Tools         │    │   - Web Search   │
│   (tools.py)    │    │   - Wikipedia    │
└─────────────────┘    │   - File Saver   │
                       └──────────────────┘
```

### Core Components

- **`main.py`**: Entry point containing the agent configuration, prompt template, and execution logic
- **`tools.py`**: Tool definitions for web search, Wikipedia queries, and file operations
- **`ResearchResponse`**: Pydantic model ensuring structured output format
- **Agent Executor**: LangChain component that orchestrates tool usage and response generation

## 🛠️ Installation

### Prerequisites

- Python 3.10+
- Virtual environment (recommended)

### Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Tusharbecoding/research-agent
   cd research-agent
   ```

2. **Create and activate virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the project root:
   ```env
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

## 📖 Usage

### Basic Usage

Run the research agent:

```bash
python main.py
```

The agent will prompt you with: `"What can I help you research?"`

Enter your research query, and the agent will:

1. Analyze your query
2. Determine the best research tools to use
3. Search the web and/or Wikipedia
4. Synthesize findings into a structured response
5. Optionally save results to a file

### Example Queries

- "What are the latest developments in artificial intelligence?"
- "Explain the causes and effects of climate change"
- "Research the history and impact of blockchain technology"
- "What are the health benefits of Mediterranean diet?"

### Output Format

The agent returns structured research results:

```python
{
    "topic": "Your research topic",
    "summary": "Comprehensive summary of findings",
    "sources": ["list", "of", "source", "urls"],
    "tools_used": ["search", "wiki_tool", "save_to_file"]
}
```

## 🔧 Available Tools

### 1. Web Search Tool

- **Purpose**: Searches the internet using DuckDuckGo
- **Use Case**: Current events, latest information, diverse perspectives
- **Source**: Real-time web results

### 2. Wikipedia Tool

- **Purpose**: Queries Wikipedia for encyclopedic information
- **Use Case**: Historical facts, scientific concepts, biographical information
- **Configuration**: Returns top result with 100 character limit for focused responses

### 3. File Saver Tool

- **Purpose**: Saves research output to local files
- **Features**:
  - Automatic timestamping
  - Appends to existing files
  - Formatted output with headers
- **Default filename**: `research_output.txt`

## 🎯 Key Features Explained

### Intelligent Tool Selection

The agent automatically determines which tools to use based on your query. For example:

- Historical topics → Prioritizes Wikipedia
- Current events → Emphasizes web search
- Comprehensive research → Uses multiple tools

### Structured Response Generation

Using Pydantic models ensures consistent output format, making it easy to:

- Parse results programmatically
- Integrate with other systems
- Maintain data quality

### Verbose Execution

The agent runs in verbose mode, allowing you to see:

- Which tools are being called
- How the agent reasons about your query
- The step-by-step research process

## 📁 Project Structure

```
research-agent/
├── main.py              # Main application entry point
├── tools.py             # Research tool definitions
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── .env                # Environment variables (create this)
└── venv/               # Virtual environment
```

## 🔒 Environment Variables

| Variable            | Description                              | Required |
| ------------------- | ---------------------------------------- | -------- |
| `ANTHROPIC_API_KEY` | Your Anthropic API key for Claude access | Yes      |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Dependencies

- **langchain**: Core framework for building the agent
- **langchain-anthropic**: Anthropic Claude integration
- **langchain-community**: Community tools (Wikipedia, DuckDuckGo)
- **pydantic**: Data validation and structured outputs
- **python-dotenv**: Environment variable management
- **duckduckgo-search**: Web search functionality
- **wikipedia**: Wikipedia API access

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your Anthropic API key is correctly set in the `.env` file
2. **Import Errors**: Verify all dependencies are installed with `pip install -r requirements.txt`
3. **Network Issues**: Check internet connection for web search and Wikipedia access
4. **File Permission Errors**: Ensure write permissions for output file directory

### Debug Mode

The agent runs with `verbose=True` by default, providing detailed execution logs to help diagnose issues.

## 🙏 Acknowledgments

- Built with [LangChain](https://langchain.com/) framework
- Powered by [Anthropic Claude](https://www.anthropic.com/) AI
- Web search via [DuckDuckGo](https://duckduckgo.com/)
- Encyclopedia data from [Wikipedia](https://www.wikipedia.org/)
