from langchain_community.document_loaders import PyPDFLoader
# PyPDFLoader converts the pdf pages into langchain Document objects
# per page = 1 Document Object, each document object contains 2 things, -> page_content, metadata
# page_content : extracted text, metadata: info such as source file and page number
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Phase 1 of RAG: document Loading
loader = PyPDFLoader("data/os_notes.pdf")

documents = loader.load()

print(f"total pages loaded: {len(documents)}")

print(documents[0].page_content[:500])
print(documents[0].metadata)

# Phase 2: Document/Text Chunking
# why is chunking used? coz, individual pages might contain multiple topics
# We will be using RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 100
)

chunks = text_splitter.split_documents(documents)

print("Original documents:", len(documents))
print("Total chunks:", len(chunks)) # for the example document, there are 26 chunks

print("\nFirst chunk:")
print(chunks[0].page_content)

print("\nMetadata:")
print(chunks[0].metadata)

# for the 26 chunks, our model should be able to semantically search them for the asked question
# next step: building the semantic search system
# Phase 3: Vector Embeddings using a vector database
# converts the text into numerical vectors
# vector database that we will be using: chroma database and the embedding model: Google's embedding model

