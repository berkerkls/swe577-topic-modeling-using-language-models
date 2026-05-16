import os
import time
import json
import random
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from dataset import load_data

load_dotenv()

# config
SAMPLES_PER_CATEGORY = 10
MAX_CHARS = 5000
RANDOM_SEED = 42
SYSTEM_PROMPT = Path("prompt.md").read_text(encoding="utf-8")

# data
data = load_data()
docs = data['docs']
labels = data['labels']
category_names = data['category_names']
doc_ids = data['doc_ids']

# output schema
class TopicResult(BaseModel):
    topic: str = Field(description="Short topic label (2-4 words)")
    confidence: float = Field(description="Confidence score between 0.0 and 1.0")
    keywords: list[str] = Field(description="Three key words from the text")

# agent
agent = Agent(
    'google-gla:gemini-2.5-flash-lite',
    output_type=TopicResult,
    system_prompt=SYSTEM_PROMPT
)


# sample docs
random.seed(RANDOM_SEED)

category_indices = defaultdict(list)
for i, label in enumerate(labels):
    category_indices[label].append(i)

sample_indices = []
for category_id, indices in category_indices.items():
    selected = random.sample(indices, min(SAMPLES_PER_CATEGORY, len(indices)))
    sample_indices.extend(selected)

# mix docs from different categories
random.shuffle(sample_indices)

TOTAL_SAMPLES = len(sample_indices)
print(f"Stratified sample: {SAMPLES_PER_CATEGORY} per category × {len(category_names)} = {TOTAL_SAMPLES} docs")

# extract topic for each document
start = time.time()
results = []

# DELAY_BETWEEN_CALLS = 4.5  # rate limit

for i, idx in enumerate(sample_indices):
    doc = docs[idx][:MAX_CHARS]
    true_category = category_names[labels[idx]]

    try:
        result = agent.run_sync(f"Analyze this text:\n\n{doc}")
        topic_data = result.output

        results.append({
            "doc_index": int(idx),
            "doc_id": doc_ids[idx],
            "topic": topic_data.topic,
            "confidence": topic_data.confidence,
            "keywords": topic_data.keywords,
            "true_category": true_category
        })

        print(f"[{i+1}/{TOTAL_SAMPLES}] {topic_data.topic} (true: {true_category})")
    except Exception as e:
        print(f"[{i+1}/{TOTAL_SAMPLES}] Error: {e}")
        results.append({
            "doc_index": int(idx),
            "doc_id": doc_ids[idx],
            "topic": "Error",
            "confidence": 0.0,
            "keywords": [],
            "true_category": true_category
        })
    # time.sleep(DELAY_BETWEEN_CALLS)
processing_time = time.time() - start

# analystics
category_stats = defaultdict(lambda: {"count": 0, "predictions": []})
for r in results:
    category_stats[r['true_category']]['count'] += 1
    category_stats[r['true_category']]['predictions'].append(r['topic'])

# save output
output = {
    "model": "Prompt-based (Gemini 2.5 Flash)",
    "framework": "PydanticAI",
    "dataset": "20 Newsgroups (stratified sample)",
    "sampling_strategy": "Stratified - equal samples per category",
    "samples_per_category": SAMPLES_PER_CATEGORY,
    "num_documents_processed": TOTAL_SAMPLES,
    "total_dataset_size": len(docs),
    "max_chars_per_doc": MAX_CHARS,
    "random_seed": RANDOM_SEED,
    "processing_time_seconds": round(processing_time, 2),
    "avg_time_per_doc": round(processing_time / TOTAL_SAMPLES, 2),
    "timestamp": datetime.now().isoformat(),
    "results": results,
    "category_stats": {k: dict(v) for k, v in category_stats.items()}
}

# JSON
os.makedirs("outputs", exist_ok=True)
with open("outputs/prompt_results.json", "w") as f:
    json.dump(output, f, indent=2)

# TXT
with open("outputs/prompt_results.txt", "w") as f:
    f.write("=" * 70 + "\n")
    f.write("Prompt-based Topic Modeling Results (Gemini + PydanticAI)\n")
    f.write("=" * 70 + "\n\n")
    f.write(f"Model           : Gemini 2.5 Flash\n")
    f.write(f"Framework       : PydanticAI\n")
    f.write(f"Dataset         : 20 Newsgroups\n")
    f.write(f"Sampling        : Stratified ({SAMPLES_PER_CATEGORY} per category)\n")
    f.write(f"Total samples   : {TOTAL_SAMPLES} / {len(docs)} docs\n")
    f.write(f"Max chars/doc   : {MAX_CHARS}\n")
    f.write(f"Random seed     : {RANDOM_SEED}\n")
    f.write(f"Total time      : {processing_time:.2f} seconds\n")
    f.write(f"Avg per doc     : {processing_time/TOTAL_SAMPLES:.2f} seconds\n")
    f.write(f"Timestamp       : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

    f.write("-" * 70 + "\n")
    f.write("RESULTS BY CATEGORY\n")
    f.write("-" * 70 + "\n\n")

    for category, stats in sorted(category_stats.items()):
        f.write(f"📂 {category} ({stats['count']} docs)\n")
        for pred in stats['predictions']:
            f.write(f"   → {pred}\n")
        f.write("\n")

    f.write("-" * 70 + "\n")
    f.write("DETAILED RESULTS\n")
    f.write("-" * 70 + "\n\n")

    for i, r in enumerate(results):
        f.write(f"Document {i+1}\n")
        f.write(f"  True Category : {r['true_category']}\n")
        f.write(f"  Predicted     : {r['topic']}\n")
        f.write(f"  Confidence    : {r['confidence']:.2f}\n")
        f.write(f"  Keywords      : {', '.join(r['keywords'])}\n\n")

print(f"\n✓ Results saved:")
print(f"  - outputs/prompt_results.json")
print(f"  - outputs/prompt_results.txt")
print(f"\nTotal time: {processing_time:.2f} s ({processing_time/60:.1f} min)")
print(f"Per document: {processing_time/TOTAL_SAMPLES:.2f} s")