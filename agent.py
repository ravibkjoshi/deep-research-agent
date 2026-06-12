import os
from dotenv import load_dotenv

from rich.console import Console
from rich.markdown import Markdown

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langchain.agents import create_agent

load_dotenv()

console = Console()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

search = TavilySearch(
    max_results=8,
    topic="general"
)

SYSTEM_PROMPT = """
You are a deep research assistant.

Your job is to research the user's topic using credible, reputable, and current sources.

Source rules:
- Prefer primary sources, official websites, government sources, academic institutions, research papers, respected news outlets, industry reports, company documentation, and reputable analysts.
- Avoid low-quality blogs, SEO spam, random forums, unsourced claims, thin affiliate content, and promotional pages unless clearly labeled as such.
- If a company, product, law, price, market, technology, or trend may have changed recently, use current sources.
- If sources disagree, explain the disagreement instead of forcing one conclusion.
- Do not make unsupported claims.
- Do not invent citations, URLs, numbers, customers, competitors, pricing, or market facts.
- If the evidence is weak, outdated, or uncertain, say that clearly.

Research requirements:
- Explain the current state of the topic.
- Identify the most important current trends.
- Explain where the topic appears to be going next.
- Include practical implications where useful.
- Cite sources directly in the response using source names and URLs.
- Separate confirmed facts from reasonable analysis or speculation.

Output format:
- Start with a short executive summary.
- Then provide the current state.
- Then list key trends.
- Then explain where the topic may be heading.
- Then give practical implications.
- End with a short final takeaway.
- Include a "Sources" section at the end with source names and URLs.
"""

agent = create_agent(
    model=llm,
    tools=[search],
    system_prompt=SYSTEM_PROMPT
)

research_topic = input("What do you want to research? ").strip()

if not research_topic:
    raise ValueError("Please enter a research topic.")

user_prompt = f"""
Research this topic: {research_topic}

Use credible, reputable, and current sources.

Please include:
1. A short executive summary
2. The current state of the topic
3. Key current trends
4. Where the topic appears to be going next
5. Practical implications
6. Citations with source names and URLs
7. A final takeaway

Avoid unsupported claims, low-quality blogs, vague summaries, and uncited statistics.
If something is uncertain, speculative, or based on limited evidence, say so clearly.
"""

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    }
)

final_content = result["messages"][-1].content

if isinstance(final_content, list):
    final_text = "\n".join(
        item.get("text", "")
        for item in final_content
        if isinstance(item, dict) and item.get("type") == "text"
    )
else:
    final_text = str(final_content)

console.print("\n[bold cyan]Research Summary[/bold cyan]\n")
console.print(Markdown(final_text))