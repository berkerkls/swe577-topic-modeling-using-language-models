from dataset import load_data

data = load_data()
docs = data['docs']


print(f"Toplam doküman sayısı: {len(docs)}")  # Toplam doküman sayısı: 18846

# bag of words

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(
    max_df=0.95,  # En fazla %95 dokümanda geçen kelimeler
    min_df=2,  # En az 2 dokümanda geçen kelimeler
    stop_words='english',  # İngilizce stop words'leri kaldır
    max_features=5000 # En sık kullanılan 1000 kelime
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

# lda topicleri

feature_names = vectorizer.get_feature_names_out()
topics = []
for i, topic in enumerate(lda.components_):
    top_words = [feature_names[j] for j in topic.argsort()[:-11:-1]]
    topics.append({
        "topic_id": i,
        "top_words": top_words
    })

output = {
    "model": "LDA",
    "dataset": "20 Newsgroups",
    "num_documents": len(docs),
    "num_topics": 10,
    "training_time_seconds": round(training_time, 2),
    "timestamp": datetime.now().isoformat(),
    "topics": topics
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


print(f"\n✓ Sonuçlar kaydedildi:")
print(f"  - outputs/lda/lda_results.json")
print(f"  - outputs/lda/lda_results.txt")
print(f"\nSüre: {training_time:.2f} sn")    