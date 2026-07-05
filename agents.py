from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from tools import web_search,scrape_url
from dotenv import load_dotenv
import os

load_dotenv()

MISTRAL_API_KEY = os.environ["MISTRAL_API_KEY"]

def get_llm():
    return ChatMistralAI(
        model_name="mistral-small-latest",
        api_key=MISTRAL_API_KEY,
        temperature=0.3

    )

def build_search_agent():
    return create_agent(
        model=get_llm(),
        tools=[web_search]    )

def build_reader_agent():
    return create_agent(
        model=get_llm(),
        tools=[scrape_url]
    )


writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a skilled research writer. Given raw research notes from web searches "
        "and scraped pages, produce a clear, well-structured report. "
        "Synthesize the information into a coherent narrative — do not just list sources. "
        "Use markdown headings and bullet points where helpful. "
        "Cite source URLs inline when referencing specific facts. "
        "If the research is incomplete or contradictory, note the gaps honestly.",
    ),
    (
        "human","""Write a report based on the topic below
        Topic : {topic}
        Research Gathered:
        {research}

        Structured the repost as: 
        - Introduction
        - Main Body
        - Conclusion
        - References
        Be concise and to the point.
        """
    ),
])

writer_chain = writer_prompt|get_llm()|StrOutputParser()

critique_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a skilled research writer. Given raw research notes from web searches "
        "and scraped pages, produce a clear, well-structured report. "
        "Synthesize the information into a coherent narrative — do not just list sources. "
        "Use markdown headings and bullet points where helpful. "
        "Cite source URLs inline when referencing specific facts. "
        "If the research is incomplete or contradictory, note the gaps honestly.",
    ),
    (
        "human",
        """Critique the following report based on the topic below
        "Report" : {report}

        Critique the report and suggest improvements.
        Score the report on a scale of 1 to 10.
        Strengths of the report:
        Ares to improve the report:
        one line verbose description of the report.
        """
    ),
])

critique_chain = critique_prompt|get_llm()|StrOutputParser()

