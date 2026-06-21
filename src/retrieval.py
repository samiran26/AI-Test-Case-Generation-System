from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings


def retrieve_context(query):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = db.similarity_search(
        query,
        k=3
    )

    context = ""

    for doc in docs:

        context += doc.page_content

        context += "\n\n"

    return context


if __name__ == "__main__":

    query = input(
        "Enter requirement/query: "
    )

    context = retrieve_context(
        query
    )

    print("\nRetrieved Context:\n")

    print(context)