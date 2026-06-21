from langchain_community.document_loaders import PyPDFLoader


def load_documents(path):

    loader = PyPDFLoader(path)

    documents = loader.load()

    return documents


if __name__ == "__main__":

    docs = load_documents("data/requirement_example.pdf")

    print(f"Pages loaded: {len(docs)}")

    print(docs[0].page_content)