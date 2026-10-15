from vector_store import get_vector_store
# role of the retriever is to retrieve chunks from existing chunks in the database
# for the 26 chunks, our model should be able to semantically search them for the asked question
# next step: building the semantic search system

def retrieve_documents(query, k=3):
    vector_store = get_vector_store()

    results = vector_store.similarity_search(
        query,
        k=k
    )

    return results

if __name__ == "__main__":

    question = (
        "Which CPU scheduling algorithm "
        "uses a time quantum?"
    )

    documents = retrieve_documents(question)

    for i, doc in enumerate(documents, start=1):

        print(f"\nResult {i}")

        print("Source:", doc.metadata.get("source"))
        print("Page:", doc.metadata.get("page_label"))

        print("Content:")
        print(doc.page_content)