from pathlib import Path

from ocr.ocr_engine import extract_text
from ingestion.chunker import chunk_text
from embeddings.embedder import EmbeddingModel
from vectorstore.chroma_store import ChromaStore


image_dir = Path("data/images")
output_dir = Path("output/ocr")

output_dir.mkdir(
    parents=True,
    exist_ok=True
)

all_chunks = []

print("Starting OCR Pipeline...")

for image_file in image_dir.glob("*"):

    text = extract_text(
        str(image_file)
    )

    output_file = output_dir / f"{image_file.stem}.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"OCR Saved: {output_file}")

    chunks = chunk_text(
        text,
        image_file.name
    )

    all_chunks.extend(chunks)

print("Generating Embeddings...")

embedder = EmbeddingModel()

texts = [
    chunk.page_content
    for chunk in all_chunks
]

embeddings = embedder.encode(texts)

print("Creating ChromaDB Store...")

vector_store = ChromaStore()

vector_store.add_documents(
    all_chunks,
    embeddings
)

print("Pipeline Completed Successfully")