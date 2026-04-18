# LSA (Latent Semantic Analysis) — Reading Notes

**Paper:** Deerwester et al. (1990) — Indexing by Latent Semantic Analysis  
**Source:** `papers/deerwester1990_lsa.pdf`

---

## 1. Core Idea
> LSA is primarily used to overcome synonymy and polysemy issues that traditional word-based search methods cannot address. It processes data from a Document-Term Matrix
> using a mathematical method called SVD. By using this technique, it aims to capture conceptual similarities between terms and documents.

## 2. How It Works
### Input
- This input has words in its rows and documents in its columns. Each data cell represents the frequency of a word's occurrence in a document. It is a structured sparse matrix.

### Steps
1. Build the Term-Document Matrix
2. Apply Singular Value Decomposition (SVD)
3. Reduce Dimensionality 

### Output
- A ranked list of documents ordered by their similarity to the query. Even documents that share no common words with the query can appear in the results as long as they are close
- to the query in the semantic space.

## 3. Strengths
#### Solves the synonymy problem: 
Two words like "access" and "retrieval" can end up close to each other in the semantic space, even if they never appear in the same document.
#### New documents and queries can be added without recomputation: 
Instead of running SVD from scratch, new items can be placed into the existing semantic space using a technique called "fold-in".
