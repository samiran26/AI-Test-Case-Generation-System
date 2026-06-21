from langchain_text_splitters import RecursiveCharacterTextSplitter
from loader import load_documents


def create_chunks():

    docs = load_documents("data/requirement_example.pdf")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=250,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    return chunks


if __name__ == "__main__":

    chunks = create_chunks()

    print(f"Total chunks: {len(chunks)}")

    print("\n----- Chunk 1 -----\n")

    print(chunks[0].page_content)

    if len(chunks) > 1:

        print("\n----- Chunk 2 -----\n")

        print(chunks[1].page_content)