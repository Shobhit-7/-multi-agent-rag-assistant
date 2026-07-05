from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

# Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def load_and_chunk(pdf_path):
    """
    PDF load karke chunks me divide karega
    """

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    if os.path.getsize(pdf_path) == 0:
        raise ValueError("PDF file is empty")

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)
    return chunks


def create_vector_store(pdf_path):
    """
    PDF -> chunks -> embeddings -> FAISS DB
    """
    chunks = load_and_chunk(pdf_path)

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local("vector_db")

    print("\nVector DB created successfully!")
    print(f"Total chunks stored: {len(chunks)}")


def load_vector_store():
    """
    Existing FAISS DB load
    """
    if not os.path.exists("vector_db"):
        raise FileNotFoundError(
            "vector_db folder not found. Pehle create_vector_store run karo."
        )

    db = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db


def get_context(query, k=3):
    """
    User query ke liye top-k relevant chunks return karega
    """
    db = load_vector_store()

    docs = db.similarity_search(query, k=k)

    context = []
    for i, doc in enumerate(docs):
        context.append(f"Chunk {i+1}:\n{doc.page_content}")

    return "\n\n".join(context)


if __name__ == "__main__":
    # YOUR PDF
    pdf_path = os.path.join("docs", "resume.pdf")

    print("Current Folder:", os.getcwd())
    print("PDF Exists:", os.path.exists(pdf_path))
    print("PDF Path:", pdf_path)

    # Vector DB create only first time
    if not os.path.exists("vector_db"):
        create_vector_store(pdf_path)

    query = input("\nEnter query: ")
    result = get_context(query)

    print("\nRelevant Context:\n")
    print(result)