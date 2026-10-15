from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from vector_store import get_vector_store
# PyPDFLoader converts the pdf pages into langchain Document objects
# per page = 1 Document Object, each document object contains 2 things, -> page_content, metadata
# page_content : extracted text, metadata: info such as source file and page number
# there are 2 steps: 
# 1. Indexing: When documents are added or updated -> loading, chunking, embedding and storing
# 2. Retrieval: Whenever the user asks a question -> searching existing vectors for relevant chunks

def ingest_pdf(file_path):
    loader = PyPDFLoader(str(file_path))# document loading
    documents = loader.load()

    print(f"Pages loaded: {len(documents)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)# document chunking

    print(f"Chunks generated: {len(chunks)}")

    vector_store = get_vector_store()

    vector_store.add_documents(chunks)# vector embedding the chunks created and stored in the chroma db

    print("Documents indexed successfully!")


if __name__ == "__main__":

    pdf_path = Path("data/os_notes.pdf")

    ingest_pdf(pdf_path)