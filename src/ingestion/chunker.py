from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_text(text, source_name):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", " "]
    )

    chunks = splitter.create_documents([text])

    for idx, chunk in enumerate(chunks):
        chunk.metadata = {
            "source": source_name,
            "chunk_id": idx
        }

    return chunks