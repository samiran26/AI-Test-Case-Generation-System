from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings

from chunking import create_chunks


def create_vector_db():

    chunks = create_chunks()

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    db.save_local("faiss_index")

    return db


if __name__ == "__main__":

    create_vector_db()

    print("Vector database created successfully.")