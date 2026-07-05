import streamlit as st
from pipeline import pipeline

st.set_page_config(
    page_title="AgentFlow AI",
    layout="wide"
)

# Session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 AgentFlow AI")
st.caption("Multi-Agent Research Assistant with RAG")

# Sidebar
with st.sidebar:
    st.header("Controls")
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.subheader("Agent Status")
    search_box = st.empty()
    rag_box = st.empty()
    reader_box = st.empty()
    writer_box = st.empty()
    critic_box = st.empty()

# Show old chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask something...")

if prompt:
    # User message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # AI response
    with st.chat_message("assistant"):
        with st.spinner("Agents Working..."):
            rag_box.success("RAG Loaded")
            search_box.info("Searching Web...")

            result = pipeline(
                prompt,
                st.session_state.messages
            )

            search_box.success("Search Done")
            reader_box.success("Reader Done")
            writer_box.success("Writer Done")
            critic_box.success("Critique Done")

            response = result["report"]
            critique = result["critique"]

            st.markdown(response)
            st.markdown("---")
            st.markdown("### Critique")
            st.markdown(critique)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })