from dataset import load_data

data = load_data()
docs = data['docs']
doc_ids = data['doc_ids']
labels = data['labels']
category_names = data['category_names']


print(f"Total number of documents: {len(docs)}")  # Total number of documents: 18846

# bag of words

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(
    max_df=0.95,  # words appearing in at most 95% of documents
    min_df=2,  # words appearing in at least 2 documents
    stop_words='english',  # remove English stop words
    max_features=5000 # top 5000 most frequent words
    )  

dtm = vectorizer.fit_transform(docs)

# lda model

from sklearn.decomposition import LatentDirichletAllocation
import time
import json
from datetime import datetime

start = time.time()
lda = LatentDirichletAllocation(n_components=10, random_state=42,max_iter=20)
lda.fit(dtm)
training_time = time.time() - start

# lda topics

feature_names = vectorizer.get_feature_names_out()
topics = []
for i, topic in enumerate(lda.components_):
    top_words = [feature_names[j] for j in topic.argsort()[:-21:-1]]
    topics.append({
        "topic_id": i,
        "top_words": top_words
    })

# Per-document topic assignment (argmax over topic distribution)
doc_topic = lda.transform(dtm)
assignments = [
    {
        "doc_id": doc_ids[i],
        "true_category": category_names[labels[i]],
        "topic_id": int(doc_topic[i].argmax()),
        "topic_prob": float(doc_topic[i].max()),
    }
    for i in range(len(docs))
]

output = {
    "model": "LDA",
    "dataset": "20 Newsgroups",
    "num_documents": len(docs),
    "num_topics": 10,
    "training_time_seconds": round(training_time, 2),
    "timestamp": datetime.now().isoformat(),
    "topics": topics,
    "assignments": assignments,
}


with open("outputs/lda/lda_results.json", "w") as f:
    json.dump(output, f, indent=2)


with open("outputs/lda/lda_results.txt", "w") as f:
    f.write("=" * 60 + "\n")
    f.write("LDA Topic Modeling Results\n")
    f.write("=" * 60 + "\n\n")
    f.write(f"Dataset: 20 Newsgroups\n")
    f.write(f"Documents: {len(docs)}\n")
    f.write(f"Topics: 10\n")
    f.write(f"Training time: {training_time:.2f} seconds\n")
    f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    f.write("-" * 60 + "\n")
    f.write("TOPICS\n")
    f.write("-" * 60 + "\n\n")
    for t in topics:
        f.write(f"Topic {t['topic_id']}: {', '.join(t['top_words'])}\n")


print(f"\n✓ Results saved:")
print(f"  - outputs/lda/lda_results.json")
print(f"  - outputs/lda/lda_results.txt")
print(f"\nDuration: {training_time:.2f} s")