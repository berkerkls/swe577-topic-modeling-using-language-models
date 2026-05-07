# TopicGPT — Reading Notes

**Paper:** Pham et al. (2024)-TopicGPT: A Prompt-based Topic Modeling Framework
**Source:** [https://arxiv.org/abs/2311.01449](https://arxiv.org/pdf/2311.01449)


## 1. Core Idea
TopicGPT uses LLMs directly through prompts to generate topics as natural language labels with descriptions.

## 2. How It Works

### Pipeline (3 Steps)
1. **Generation** — A sample of documents is fed to the LLM. The model is prompted to assign existing topics, building a topic list while it processes more documents.
2. **Refinement** — Similar or redundant topics are merged, and rare topics are removed to produce a clean topic set.
3. **Assignment** — Given a new document, the LLM assigns it to one or more topics and provides a supporting quote from the document to justify its assignment.

## 3. Strengths
- **Human-readable topics**: Produces labels and descriptions.
- **Controllable**: Users can add constraints, edit topics, and guide the model without retraining.
- **Verifiable**: Provides document quotes to support topic assignments.
- **Hierarchical**: Can generate subtopics for deeper exploration.
