# dataset.py
from sklearn.datasets import fetch_20newsgroups
import pickle

def load_and_save():
    """Download the 20newsgroups dataset and save it to disk"""
    print("Downloading dataset...")
    newsgroups = fetch_20newsgroups(
        subset='all',
        remove=('headers', 'footers', 'quotes')
    )

    data = {
        'docs': newsgroups.data,
        'labels': newsgroups.target,
        'category_names': newsgroups.target_names
    }

    with open('data/data.pkl', 'wb') as f:
        pickle.dump(data, f)

    print(f"Saved: {len(data['docs'])} documents")
    return data


def load_data():
    """Quickly load from disk"""
    with open('data/data.pkl', 'rb') as f:
        return pickle.load(f)


if __name__ == "__main__":
    load_and_save()