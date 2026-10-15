from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

def get_vector_store():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

    vector_store = Chroma(# this command connects to an existing database   
        collection_name="ai_tutor_notes",
        embedding_function=embeddings,
        persist_directory="./chroma_db"
    )

    return vector_store

# since the vector database is created, we should not run the Chrome.from_documents(...) command, to avoid
# duplicates in the database
# what is similarity search or semantic search?
# user asks a question -> query embedding -> similarity search -> find stored vectors closest to the query
# return top k=3 chunks
# current complete step: retrievel step, next step that comes is the generation part