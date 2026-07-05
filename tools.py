from langchain.tools import tool
from langchain_mistralai import ChatMistralAI
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
from typing import Annotated,TypedDict
from langgraph.graph import StateGraph,END
from rich import print
import os
from dotenv import load_dotenv

load_dotenv()
TAVILY_API_KEY = os.environ["TAVILY_API_KEY"]


tavily = TavilyClient(api_key=TAVILY_API_KEY)
class AgentState(TypedDict):
    research_data:str

@tool
def web_search(query:str)-> str:
    """Search the web for recent and realiable information on a given query using Tavily.Returns Titles , URLs , Content"""
    response = tavily.search(
        query=query,
        search_depth="advanced",
        max_results=2
    )
    data_points = []
    for r in response.get("results"):
        data_points.append(f"title:{r.get('title')}\nURL:{r.get('url')}\nContent:{r.get('content')}")
    return "\n-----\n".join(data_points)


@tool
def scrape_url(url:str)-> str:
    """Scrape a website for its content.Returns the content of the website. Max 3000 characters."""
    try:
        response = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style","nav","footer"]):
            tag.decompose()
        return soup.get_text(separator="\n", strip=True)[:3000]
    except Exception as e:
        return f"Error scraping website: {e}"

