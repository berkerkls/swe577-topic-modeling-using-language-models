# NMF (Non-Negative Matrix Factorization) — Reading Notes

**Paper:** Lee & Seung (1999) — Learning the parts of objects by NMF  
**Source:** `papers/lee1999_nmf.pdf`

---

## 1. Core Idea
> NMF takes a big table of data and breaks it down into two smaller tables: one that holds the building blocks, and one that shows how much of each block is used in each item.

## 2. How It Works
### Input
- A table of non-negative numbers. Rows are features as words and columns are items as documents. For text value, each cell simply represent how many times a word appears in a document.

### Steps
1. Start with two random tables
2. Keep updating W and H step by step
3. Stop when the approximation is good enough

### Output
#### W table: 
A collection of learned parts. For faces, these are patches like eyes, noses, and mouths. For text, these are topics, each represented by a group of related words.
#### H Table:
For each document, a list of how strongly each part is used. Most values are zero so each item is built from just a few parts.

## 3. Strengths
#### Learns real parts: 
It finds pieces you can actually recognize instead of abstract math directions that mean nothing.
#### Handles words with multiple meanings:
It can tell apart different meanings of the same word by looking at which other words appear around it in different contexts.
#### Produces clean results:
Each item is built from only a few parts so output is easy to read and fast to work with.

## 4. Connection to Other Methods
- NMF vs LSA: 
> Both methods break a word-document table into smaller pieces, but LSA can use negative numbers (making the results hard to read),
> while NMF only adds things up (so the results look like real topics). LSA gives one best answer and is better for search, but NMF is easier to understand
> when you want to see the topics in your data.
