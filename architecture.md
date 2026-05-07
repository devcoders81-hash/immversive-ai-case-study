
---

# architecture.md

```md
# Architecture Documentation

# System Overview

This project implements a production-oriented Conversational RAG pipeline for Indic manuscript understanding.

The system performs:

1. OCR extraction from manuscript images
2. Image preprocessing
3. Text normalization and chunking
4. Embedding generation
5. Hybrid retrieval using ChromaDB + BM25
6. Grounded answer generation using Groq LLM
7. Conversational querying using Streamlit

---

# High-Level Architecture

```text
                +-------------------+
                | Manuscript Images |
                +---------+---------+
                          |
                          v
                +-------------------+
                | Image             |
                | Preprocessing     |
                | OpenCV            |
                +---------+---------+
                          |
                          v
                +-------------------+
                | OCR Engine        |
                | EasyOCR           |
                +---------+---------+
                          |
                          v
                +-------------------+
                | Text Chunking     |
                | Metadata Builder  |
                +---------+---------+
                          |
                          v
                +-------------------+
                | Embedding Model   |
                | BGE-M3            |
                +---------+---------+
                          |
                          v
                +-------------------+
                | Hybrid Retrieval  |
                | ChromaDB + BM25   |
                +---------+---------+
                          |
                          v
                +-------------------+
                | Groq LLM          |
                | Grounded Prompt   |
                +---------+---------+
                          |
                          v
                +-------------------+
                | Streamlit UI      |
                +-------------------+
