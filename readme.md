# Deep Research Agent

A local AI research agent built with Python, LangChain, Google Gemini, and Tavily Search.

This project demonstrates how a large language model can be connected to external search tools and used as a research agent instead of a basic chatbot. The agent accepts a research topic from the command line, searches for current information, prioritizes credible sources, and returns a structured research summary with citations.

## What This Project Demonstrates

- Building an AI agent with LangChain
- Connecting Google Gemini to a Python application
- Using Tavily Search as an external research tool
- Secure API key management with `.env`
- Running an AI agent locally from the command line
- Prompting an agent to prioritize credible and reputable sources
- Returning structured research output instead of raw model responses
- Formatting final output cleanly using Rich Markdown

## Project Goal

The goal of this project is to show how an AI agent can research a user-provided topic and return a useful, structured answer that includes:

- A short executive summary
- The current state of the topic
- Key current trends
- Where the topic appears to be heading
- Practical implications
- Source names and URLs
- A final takeaway

The system prompt is designed to reduce unsupported claims by instructing the agent to prefer credible, reputable, and current sources.

## How It Works

The agent follows this basic workflow:

1. Loads API keys from a local `.env` file.
2. Initializes Google Gemini using LangChain.
3. Connects Tavily Search as an external research tool.
4. Prompts the user to enter a research topic.
5. Sends the research request to the LangChain agent.
6. The agent searches for relevant current information.
7. The response is formatted and printed in the terminal.

## Tech Stack

- Python
- LangChain
- Google Gemini
- Tavily Search
- python-dotenv
- Rich

## Project Structure

```text
deep-research-agent/
├── .env
├── .gitignore
├── agent.py
├── README.md
└── requirements.txt
```

## How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/ravibkjoshi/deep-research-agent.git
cd deep-research-agent
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, use:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a file named `.env` in the root of the project.

Add your API keys:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
LANGSMITH_API_KEY="your_langsmith_api_key_here" 
```

Do not commit your real `.env` file to GitHub.

### 5. Run the agent

```bash
python3 agent.py
```

The app will ask:

```text
What do you want to research?
```

Enter a research topic, for example:

```text
The Future of AI Agents
```

The agent will then return a structured research summary using Google Gemini, LangChain, and Tavily Search.
