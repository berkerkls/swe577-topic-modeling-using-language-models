# LDA (Latent Dirichlet Allocation) — Reading Notes

**Paper:** Blei, Ng & Jordan (2003) — Latent Dirichlet Allocation
**Source:** `papers/blei2003_lda.pdf`

---

## 1. Core Idea
> LDA is a model that assumes every document is a mixture of a small number of hidden topics and every topic is a mixture of words. 

## 2. How it works?

#### 1. Pick a topic mixture for the document:
> Decide what percentage of the document belongs to each topic, like "mostly sports, a bit of politics."
#### 2. For each word slot, pick a topic:
> For every word you are about to write, randomly choose one topic based on the document's mixture.
#### 3.For each chosen topic, pick an actual word:
> Once you know the topic, pick a real word from that topic's word list (from the "sports" topic, pick "goal" or "team").

## 3. Strengths
#### Properly generalizes to unseen documents:
It can handle brand new documents naturally, without any tricks, because it is built as a real probability model.
#### Avoids overfitting:
It has a fixed number of parameters no matter how big your training data gets.
#### Documents can have multiple topics:
Every document gets its own blend of topics, so one article can be part multiple topics just like real writing.

## 4. Connection to Other Methods
- LDA vs LSA:
> LSA is fast but gives abstract, hard-to-read components, while LDA is a full probability model that is slower but produces meaningful topics and can handle new documents properly.
- LDA vs NMF:
> NMF is a simpler and faster math-based method for finding topics, while LDA is a full probability model that is slower but more powerful.
