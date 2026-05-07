# Architecture Documentation

# System Overview

This project implements a production-oriented Conversational RAG pipeline for Indic manuscript understanding.

The system performs:

1. OCR extraction from manuscript images
2. Text preprocessing and normalization
3. Metadata-aware chunking
4. Embedding generation
5. Hybrid retrieval using FAISS + BM25
6. Grounded answer generation using LLMs
7. Conversational querying through Streamlit UI

---

# System Architecture

```text
                +-------------------+
                | Manuscript Images |
                +---------+---------+
                          |
                          v
                +-------------------+
                | OCR Pipeline      |
                | EasyOCR           |
                | OpenCV Processing |
                +---------+---------+
                          |
                          v
                +-------------------+
                | Text Cleaning     |
                | Unicode Normalize |
                +---------+---------+
                          |
                          v
                +-------------------+
                | Chunking Engine   |
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
                | Hybrid Retriever  |
                | FAISS + BM25      |
                +---------+---------+
                          |
                          v
                +-------------------+
                | LLM Generator     |
                | Grounded Prompt   |
                +---------+---------+
                          |
                          v
                +-------------------+
                | Streamlit UI      |
                +-------------------+