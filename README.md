# 🤖 AgentFlow AI — Multi-Agent Research Assistant

**Built by Shobhit Shukla**

AgentFlow AI is an advanced **Multi-Agent Research Assistant** that combines **RAG (Retrieval-Augmented Generation)**, **web search**, **document retrieval**, and **LLM-based reasoning** to generate high-quality research reports with automated critique.

This project simulates an **agentic AI workflow** where multiple AI agents collaborate to search, retrieve, analyze, and evaluate information before producing a final response.

---

## 🚀 Features

✅ **Multi-Agent Architecture**
Specialized AI agents handle different tasks:

* Search Agent
* Reader Agent
* Writer Agent
* Critique Agent

✅ **RAG (Retrieval-Augmented Generation)**
Upload PDFs (resume, notes, research papers) and retrieve relevant knowledge using vector search.

✅ **Web Search Integration**
Real-time web search using Tavily for up-to-date information.

✅ **Document Scraping**
Automatically extracts deep content from relevant URLs.

✅ **Conversation Memory**
Maintains chat history and context for follow-up questions.

✅ **Critique Engine**
Generated reports are evaluated and scored by a separate critique agent.

✅ **Interactive UI**
Built with Streamlit for an easy-to-use chat interface.

---

# 🏗 Architecture

```text
User Query
    ↓
Conversation Memory
    ↓
RAG Retriever (PDF / Documents)
    ↓
Search Agent (Web Search)
    ↓
Reader Agent (Scraping)
    ↓
Writer Agent (Report Generation)
    ↓
Critique Agent (Evaluation)
    ↓
Final Response
```

---

# 🛠 Tech Stack

## Languages

* Python

## AI / LLM

* LangChain
* LangGraph
* Mistral LLM
* RAG Pipeline

## Vector Database

* FAISS

## Search / Retrieval

* Tavily Search API
* BeautifulSoup
* PyPDF

## Frontend

* Streamlit

---

# 📂 Project Structure

```bash
AgentFlow-AI/
│
├── app.py              # Streamlit UI
├── pipeline.py         # Main workflow pipeline
├── agents.py           # Agent definitions
├── rag.py              # RAG pipeline
├── tools.py            # Web search + scraping tools
├── requirements.txt
│
├── docs/               # Uploaded PDFs
└── vector_db/          # FAISS vector storage
```

---

# ⚙ Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd AgentFlow-AI
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create `.env` file:

```env
TAVILY_API_KEY=your_key
MISTRAL_API_KEY=your_key
```

Get API Keys:

* Tavily API
* Mistral AI

---

# ▶ Running the Project

Run Streamlit app:

```bash
streamlit run app.py
```

Run CLI pipeline:

```bash
python pipeline.py "What AI roles suit my resume?"
```

---

# 🧠 Example Use Cases

### Resume Analysis

* What roles suit my resume?
* What are my technical skills?

### Research Assistant

* Latest AI trends in 2026
* Explain reinforcement learning

### Document QA

* Summarize uploaded PDF
* Explain chapter 4 of notes

---

# 📈 Future Improvements

* Multi-document RAG
* Voice interaction
* Authentication
* Cloud deployment
* Database persistence
* Agent monitoring dashboard
* Model routing (GPT / Claude / Mistral)

---

# 💡 Key Learnings

Through this project I gained practical experience in:

* Agentic AI systems
* LLM orchestration
* Prompt engineering
* RAG architecture
* Vector databases
* Memory management
* AI product design

---

# 👨‍💻 Author

## Shobhit Shukla

B.Tech CSE (AI & ML)


GitHub: https://github.com/shobhit-7
-- ⭐ Support

If you found this project useful, consider giving it a star.
