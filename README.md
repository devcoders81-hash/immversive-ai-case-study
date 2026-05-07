# Manuscript Conversational RAG Pipeline

A production-oriented Conversational RAG system for Indic manuscript understanding using OCR, Hybrid Retrieval, ChromaDB, and Groq LLM.

---

# Features

- OCR extraction using EasyOCR
- Image preprocessing using OpenCV
- Metadata-aware chunking
- Embedding generation using BGE-M3
- Persistent vector storage using ChromaDB
- Hybrid retrieval using BM25 + ChromaDB
- Conversational RAG using Groq LLM
- Streamlit-based UI
- OCR evaluation using CER
- Modular and scalable architecture

---

# Tech Stack

| Component | Technology |
|---|---|
| OCR | EasyOCR |
| Image Processing | OpenCV |
| Embeddings | BAAI/bge-m3 |
| Vector Database | ChromaDB |
| Sparse Retrieval | BM25 |
| LLM | Groq API |
| UI | Streamlit |
| Evaluation | jiwer |
| Language | Python 3.12 |

---

# Why EasyOCR?

PaddleOCR was initially evaluated for Indic OCR support.

EasyOCR was selected because:

- Better compatibility with Python 3.12
- Easier Windows installation
- Lower operational complexity
- Faster setup for reviewers
- Stable CPU inference

This decision prioritizes portability and reproducibility.

---

# Project Structure

```bash
manuscript_rag_project/
│
├── README.md
├── architecture.md
├── evaluation.md
├── requirements.txt
├── .env
│
├── data/
│   ├── images/
│   │   ├── page_1.png
│   │   └── page_2.png
│   │
│   └── reference_text/
│
├── output/
│   ├── ocr/
│   ├── chroma_db/
│   ├── logs/
│   └── audio/
│
├── src/
│   ├── main.py
│   │
│   ├── ocr/
│   │   ├── preprocess.py
│   │   └── ocr_engine.py
│   │
│   ├── ingestion/
│   │   └── chunker.py
│   │
│   ├── embeddings/
│   │   └── embedder.py
│   │
│   ├── vectorstore/
│   │   └── chroma_store.py
│   │
│   ├── retrieval/
│   │   └── hybrid_retriever.py
│   │
│   ├── llm/
│   │   └── groq_generator.py
│   │
│   ├── evaluation/
│   │   └── evaluate_ocr.py
│   │
│   └── ui/
│       └── streamlit_app.py
│
└── sample_outputs/
