# Tools & Applications - Survey Notes

**Date:**
**Sources:** Web search, GitHub, PyPI, official docs

---

## 1. Python Libraries / Toolkits

### LLM-Based / Neural

| Tool | Language | Methods | Link |
|------|----------|---------|------|
| **BERTopic** | Python | SBERT + UMAP + HDBSCAN + c-TF-IDF | https://maartengr.github.io/BERTopic/ |
| **FASTopic** | Python | Optimal transport + Transformer embeddings | https://github.com/bobxwu/FASTopic |
| **TopMost** | Python | Toolkit: preprocessing, training, evaluation for many models | https://github.com/BobXWu/TopMost |
| **TopicGPT** | Python | GPT-4 prompt-based topic generation and assignment | https://github.com/chtmp223/topicGPT |

### Visualization

| Tool | Purpose | Link |
|------|---------|------|
| **pyLDAvis** | Interactive LDA topic visualization | https://github.com/bmabey/pyLDAvis |
| **BERTopic built-in** | Topic bars, similarity maps, hierarchy | Built into BERTopic |

---

## 2. Real World Applications

### Healthcare
- Analyzing electronic health records and clinical notes to identify disease patterns
- Monitoring medical literature for emerging treatment approaches
- Tracking health discussions on social media (e.g., ATAM model on Twitter for discovering health topics)

### Social Media Analysis
- Brand monitoring and customer sentiment analysis
- Tracking public opinion during events (e.g., COVID-19 tweet analysis using LDA)
- Identifying emerging trends and discussions

### Business & Market Research
- Customer feedback analysis from reviews, surveys, and support tickets
- Competitor positioning tracking
- Financial news analysis for market trend detection

### Academia & Research
- Literature review automation and paper categorization
- Research trend discovery across scientific publications
- Content recommendation for researchers

### Content & Media
- News article categorization and tagging
- Personalized content recommendations
- Document organization in large archives

---

## 3. Key Observations

### Classical vs LLM-Based Tools
- Classical tools (Gensim, sklearn, MALLET) are mature, well-documented, and fast, but require preprocessing (stop words, stemming, etc.)
- LLM-based tools (BERTopic) need no preprocessing and capture semantic meaning, but are computationally heavier
- FASTopic bridges the gap - fast like classical methods but uses transformer embeddings
- TopicGPT takes a completely different approach by using LLM prompts instead of statistical methods

### Trend: Hybrid Approaches
- BERTopic can now integrate LLMs (GPT, Llama) for generating topic labels on top of its clustering pipeline
- MALLET + ChatGPT integration used in healthcare research for interpreting topics
- Combining classical speed with LLM interpretability is the current direction
