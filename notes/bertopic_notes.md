# BERTopic — Reading Notes

**Paper:** Grootendorst (2022) — BERTopic: Neural topic modeling with a class-based TF-IDF procedure
**Source:** [https://arxiv.org/abs/2203.05794](https://arxiv.org/pdf/2203.05794)
**Docs:** [https://maartengr.github.io/BERTopic/](https://maartengr.github.io/BERTopic/)


## 1. Core Idea
BERTopic is a modular topic modeling framework that converts documents into semantic embeddings, clusters them, and then extracts topic labels using TF-IDF (c-TF-IDF) method.

## 2. How It Works

### Pipeline (5 Steps)
1. **Embed documents** — Uses sentence transformers to convert each document into a vector that captures semantic meaning.
2. **Reduce dimensions** — Applies UMAP to reduce embeddings into a lower space while preserving structure.
3. **Cluster documents** — Uses HDBSCAN to group semantically similar documents into clusters. Documents that don't fit any cluster are labeled as outliers.
4. **Tokenize topics** — Applies a bag-of-words approach per cluster to prepare for topic extraction.
5. **Extract topic labels** — Finds the most representative words for each cluster, creating the final topic descriptions.

## 3. Strengths
- **Modular**: Each step (embedding, clustering, representation) can be swapped independently.
- **Semantic**: Captures meaning, not just word frequency.
- **No preprocessing needed**: Does not require stop word lists, stemming, or lemmatization.
- **Multilingual support**: Works with 50+ languages using multilingual sentence transformers.
- **Visual tools**: Built in topic visualization (topic bars, similarity maps, hierarchy).
