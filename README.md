# LangChain-Projects

Hello Folks!. This is a langchain collection of 11 of my practical projects demonstrating various applications and implementations of LangChain for language model interactions, document processing, and AI-powered functionalities.

## 📋 Project Overview

This repository contains the following LangChain implementations:

1. **Q&A Chatbot**: A conversational AI chatbot built with LangChain that can answer user queries. I used both the frontier model `gpt-4o` and open source model `ollama`. In addition you can download the response either as `pdf` or `docs` or copy as `.md` file.
2. **RAG Document Q&A**: Retrieval-Augmented Generation system for question answering on specific documents based on the uploaded documents.
3. **RAG Q&A with Conversation History**: Enhanced RAG system that maintains conversation context.
4. **SearchEngine With Tools & Agents**: Implementation of search functionality using LangChain tools and agents.
5. **Chat with SQL**: Interactive system to query databases using natural language via MySQL DB.
6. **Text Summarization**: Tool for generating concise summaries of lengthy text content.
7. **YT Video And Website Content Analysis**: System to extract and analyze content from YouTube videos and websites.
8. **MathsGPT**: Specialized implementation for mathematical problem solving.
9. **Huggingface with Langchain**: Integration of Hugging Face models with LangChain.
10. **PDF Query RAG with Langchain**: System for querying and retrieving information from PDF documents.
11. **MultiLanguage Code Assistant**: Programming assistant supporting multiple coding languages.

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NickBwalley/LangChain-Projects.git
   cd LangChain-Projects
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   .venv\Scripts\activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

# What is LangChain?

LangChain is an open-source framework designed to help developers build applications powered by LLMs. It provides tools to structure LLM interactions, manage memory, integrate APIs, and create complex workflows.

## Benefits of LangChain

- Simplifies handling prompts and responses
- Supports multiple LLM providers (OpenAI, Hugging Face, Anthropic, etc.)
- Enables memory, retrieval, and chaining multiple AI calls
- Supports building chatbots, agents, and AI-powered apps

## Why Langchain Framework?

Large language models (LLMs) like OpenAI’s GPT-4 and Hugging Face models are powerful, but using them effectively in applications requires more than just calling an API. LangChain is a framework that simplifies working with LLMs, enabling developers to create advanced AI applications with ease.

## Create and Setup `venv` in langchain

#### 1. create a `venv` using conda

```
conda create -p venv python==3.11 -y
```

#### 2. create a `requirements.txt`

- langchain
- ipykernel

#### 3. install your packages in `requirements.txt`

```
pip install -r requirements.txt
```

#### 4. confirm if a package is installed

```
pip list | findstr "name_of_package"
```

#### 5. activate the `conda environment`

```
conda activate venv
```

## 🛠️ Additional Useful Commands

### Managing the Environment

```bash
# Update pip
pip install --upgrade pip

# Install a specific package
pip install package_name

# Export requirements
pip freeze > requirements.txt

# Deactivate virtual environment
deactivate
```

### Running with Different Options

```bash
# Run with specific model options (example)
streamlit run app.py -- --model gpt-4

# Run in debug mode
streamlit run app.py -- --debug

# Run with specific API key
streamlit run app.py -- --api_key YOUR_API_KEY
```

## 🔄 API Keys and Environment Variables

Some projects might require API keys for OpenAI, Hugging Face, or other services. Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

If you have any questions or suggestions, please open an issue or you can create a pull request or contact me at nickbiiybwalley@gmail.com for any collaborations.
