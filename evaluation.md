
---

# evaluation.md

```md
# Evaluation Documentation

# Evaluation Goals

The evaluation process measures:

1. OCR quality
2. Retrieval effectiveness
3. Answer correctness
4. Response groundedness

---

# OCR Evaluation

## Metric Used

Character Error Rate (CER)

---

# Why CER?

CER measures:

- Character insertions
- Character deletions
- Character substitutions

Lower CER indicates better OCR quality.

---

# CER Formula

```text
CER = (Substitutions + Insertions + Deletions) / Total Characters
