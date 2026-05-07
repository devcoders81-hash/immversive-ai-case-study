# Manuscript Conversational RAG Pipeline

## Overview

This project implements a production-oriented Conversational RAG pipeline for Indic manuscript understanding.

The system performs:

* OCR extraction from manuscript images
* Text chunking and metadata enrichment
* Embedding generation
* Hybrid retrieval (FAISS + BM25)
* Grounded answer generation using LLMs
* Conversational interface using Streamlit

---

# Tech Stack

| Component         | Technology                    |
| ----------------- | ----------------------------- |
| OCR               | EasyOCR                       |
| Embeddings        | BAAI/bge-m3                   |
| Vector Store      | FAISS                         |
| Keyword Retrieval | BM25                          |
| LLM               | Mistral / OpenAI Compatible   |
| UI                | Streamlit                     |
| Evaluation        | jiwer + custom RAG evaluation |

---

# Why EasyOCR Instead of PaddleOCR?

PaddleOCR was initially evaluated for Indic OCR support.

EasyOCR was selected because:

* Better compatibility with Python 3.12
* Easier Windows installation
* Reduced deployment complexity
* Faster setup for reproducible execution
* Stable CPU-based inference

This decision prioritizes portability, reproducibility, and reviewer accessibility.

---

# Project Structure

```bash
repo/
├── README.md
├── architecture.md
├── evaluation.md
├── requirements.txt
├── data/
├── output/
├── sample_outputs/
└── src/
```

---

# Setup Instructions

## 1. Create Virtual Environment

### Windows

```bash
python -m venv env
```

Activate:

```bash
env\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Python Version

Recommended:

```bash
Python 3.12
```

---

# Current requirements.txt

```txt
easyocr
torch
torchvision
opencv-python
sentence-transformers
faiss-cpu
rank-bm25
transformers
streamlit
jiwer
langchain
numpy
pandas
scikit-learn
```

---

# Run OCR Pipeline

```bash
python src/main.py --step ocr
```

OCR outputs will be stored inside:

```bash
output/ocr/
```

---

# Build Embeddings + Vector Store

```bash
python src/main.py --step ingest
```

---

# Launch Streamlit Chat Interface

```bash
streamlit run src/ui/streamlit_app.py
```

---

# OCR Pipeline

The OCR pipeline performs:

1. Image preprocessing
2. Text extraction using EasyOCR
3. Text cleanup
4. File persistence

---

# Retrieval Pipeline

The retrieval system uses hybrid search:

* Dense retrieval using embeddings + FAISS
* Sparse retrieval using BM25

This improves:

* Retrieval relevance
* Semantic understanding
* Keyword matching
* Answer grounding

---

# Evaluation

## OCR Evaluation

Metric:

* Character Error Rate (CER)

## RAG Evaluation

Metrics:

* Retrieval relevance
* Faithfulness
* Groundedness
* Answer correctness

---

# Scaling Strategy

For large-scale deployment:

* Move FAISS → Milvus/Qdrant
* Add distributed embedding workers
* Use Redis caching
* Add async OCR processing
* Use GPU inference services
* Store images in object storage (S3/GCS)

---

# Assumptions

* Manuscript images exist in `data/images`
* OCR quality may vary depending on manuscript quality
* CPU execution is acceptable for assignment-scale workloads

---

# Future Improvements

* Indic language fine-tuned OCR
* Cross-encoder reranking
* Multilingual translation
* Text-to-Speech responses
* Conversation memory
* Evaluation dashboard

---

# Expected Outputs

```bash
output/
├── ocr/
├── embeddings/
├── logs/
└── audio/
```

---

# Sample Questions

* What is the manuscript about?
* Explain verse 2.
* Summarize the first section.
* What does this manuscript discuss about health?
