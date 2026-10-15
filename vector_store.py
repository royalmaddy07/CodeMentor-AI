from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from retriever import chunks

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

# vector_store = Chroma.from_documents(
#     documents=chunks,
#     embedding=embeddings,
#     collection_name="ai_tutor_notes",
#     persist_directory="./chroma_db"
# )

# print("Vector database created successfully")

# since the vector database is created, we should not run the Chrome.from_documents(...) command, to avoid
# duplicates in the database

vector_store = Chroma(
    collection_name="ai_tutor_notes",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)# this opens the existing database

query = "Which CPU scheduling algorithm uses a time quantum?"

results = vector_store.similarity_search(
    query,
    k=3
)# what is similarity search or semantic search?
# user asks a question -> query embedding -> similarity search -> find stored vectors closest to the query
# return top k=3 chunks
# current complete step: retrievel step, next step that comes is the generation part

for i, doc in enumerate(results, start=1):

    print(f"\nResult {i}")

    print("Source:", doc.metadata["source"])
    print("Page:", doc.metadata["page_label"])

    print("Content:")
    print(doc.page_content)