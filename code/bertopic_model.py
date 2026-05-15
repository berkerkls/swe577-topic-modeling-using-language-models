import time
import json
from datetime import datetime
from bertopic import BERTopic
from dataset import load_data

# data
data = load_data()
docs = data['docs']

# bertopic model

start = time.time()
topic_model = BERTopic(
    nr_topics=10,        # same number of topics as LDA (fair comparison)
    verbose=True,
    language="english"
)
topics_list, probs = topic_model.fit_transform(docs)
training_time = time.time() - start


# topics
topics = []
topic_info = topic_model.get_topic_info()

for topic_id in topic_info['Topic']:
    if topic_id == -1:  # skip the -1 outlier topic
        continue
    topic_words = topic_model.get_topic(topic_id)
    if topic_words:
        top_words = [word for word, _ in topic_words[:10]]
        topics.append({
            "topic_id": int(topic_id),
            "top_words": top_words,
            "count": int(topic_info[topic_info['Topic'] == topic_id]['Count'].values[0])
        })

# output
output = {
    "model": "BERTopic",
    "dataset": "20 Newsgroups",
    "num_documents": len(docs),
    "num_topics": len(topics),
    "training_time_seconds": round(training_time, 2),
    "timestamp": datetime.now().isoformat(),
    "topics": topics
}

with open("outputs/bertopic/bertopic_results.json", "w") as f:
    json.dump(output, f, indent=2)


with open("outputs/bertopic/bertopic_results.txt", "w") as f:
    f.write("=" * 60 + "\n")
    f.write("BERTopic Topic Modeling Results\n")
    f.write("=" * 60 + "\n\n")
    f.write(f"Dataset: 20 Newsgroups\n")
    f.write(f"Documents: {len(docs)}\n")
    f.write(f"Topics: {len(topics)}\n")
    f.write(f"Training time: {training_time:.2f} seconds\n")
    f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    f.write("-" * 60 + "\n")
    f.write("TOPICS\n")
    f.write("-" * 60 + "\n\n")
    for t in topics:
        f.write(f"Topic {t['topic_id']} ({t['count']} docs): {', '.join(t['top_words'])}\n")

# visualization
try:
    fig = topic_model.visualize_barchart(top_n_topics=10)
    fig.write_html("outputs/bertopic/bertopic_barchart.html")
    print("✓ Visualization saved: outputs/bertopic/bertopic_barchart.html")
except Exception as e:
    print(f"⚠ Visualization skipped: {e}")

print(f"\n✓ Results saved:")
print(f"  - outputs/bertopic/bertopic_results.json")
print(f"  - outputs/bertopic/bertopic_results.txt")
print(f"  - outputs/bertopic/bertopic_barchart.html")
print(f"\nDuration: {training_time:.2f} s")