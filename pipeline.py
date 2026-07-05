from rag import get_context
from agents import build_reader_agent, build_search_agent, writer_chain, critique_chain


def pipeline(topic: str, chat_history=None) -> dict:
    state = {}

    search_agent = build_search_agent()
    reader_agent = build_reader_agent()

    # -------- Conversation Memory --------
    history_text = ""
    if chat_history:
        history_text = "\n".join(
            [
                f"{msg['role']}: {msg['content']}"
                for msg in chat_history[-6:]
            ]
        )

    # ---------------- RAG ----------------
    try:
        rag_context = get_context(topic)
        state["rag_context"] = rag_context
        print("\nRAG Context Loaded Successfully")
    except Exception as e:
        print("\nRAG skipped:", e)
        state["rag_context"] = "No PDF context available"

    # ------------- Web Search ------------
    search_result = search_agent.invoke({
        "messages": [
            (
                "user",
                f"""
Conversation History:
{history_text}

Current Question:
{topic}

Find recent, reliable and detailed information.
"""
            )
        ]
    })

    state["search_results"] = search_result["messages"][-1].content

    # ------------- Reader Agent ----------
    reader_result = reader_agent.invoke({
        "messages": [
            (
                "user",
                f"""
Conversation History:
{history_text}

Question:
{topic}

Search Results:
{state['search_results'][:800]}

Pick best URL and scrape deeper content.
"""
            )
        ]
    })

    state["reader_result"] = reader_result["messages"][-1].content

    research_combined = (
        f"CHAT HISTORY:\n{history_text}\n\n"
        f"RAG CONTEXT:\n{state['rag_context']}\n\n"
        f"SEARCH RESULTS:\n{state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT:\n{state['reader_result']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined,
    })

    state["critique"] = critique_chain.invoke({
        "report": state["report"],
    })

    return state


if __name__ == "__main__":
    import sys
    topic = sys.argv[1] if len(sys.argv) > 1 else input("\nEnter topic: ")
    pipeline(topic)