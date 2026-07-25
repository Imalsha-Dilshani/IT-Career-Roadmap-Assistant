import os
from rag.loader import load_pdf
from rag.chunker import split_documents
from rag.embeddings import get_embedding_model
from rag.vectorstore import create_vector_store
from rag.retriever import create_retriever


pdf_folder = "data/documents"

pdf_files = [
    os.path.join(pdf_folder, file)
    for file in os.listdir(pdf_folder)
    if file.endswith(".pdf")
]

documents = []

for pdf in pdf_files:
    documents.extend(load_pdf(pdf))

print("PDF files loaded:", len(pdf_files))
print("Documents loaded:", len(documents))


# Split into chunks
chunks = split_documents(documents)

print("Chunks created:", len(chunks))


# Create embeddings
embeddings = get_embedding_model()


# Create FAISS database
vector_db = create_vector_store(
    chunks,
    embeddings
)

print("Vector store created")


# Test retrieval
retriever = create_retriever(vector_db)

queries = [
    "What skills are needed to become a Python developer?",
    "How can I start a cybersecurity career?",
    "What technologies should a cloud engineer learn?",
    "What skills are required for a data engineer?",
    "How can I become a UI UX designer?"
]


for query in queries:

    print("\n==============================")
    print("QUERY:", query)

    results = retriever.invoke(query)

    for doc in results[:2]:
        print("\n--- Retrieved Context ---")
        print(doc.page_content[:500])