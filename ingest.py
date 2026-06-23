import os
import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

DATA_FILE = os.path.join("Data", "medical_records_dataset (1).csv")
VECTOR_DIR = os.path.join("vector_store")
VECTORIZER_PATH = os.path.join(VECTOR_DIR, "tfidf_vectorizer.pkl")
DOCS_PATH = os.path.join(VECTOR_DIR, "documents.pkl")
EMBEDDINGS_PATH = os.path.join(VECTOR_DIR, "embeddings.npz")


def format_document(row: pd.Series) -> str:
    parts = []
    for key, label in [
        ("Disease", "Disease"),
        ("Symptoms", "Symptoms"),
        ("Diagnosis", "Diagnosis"),
        ("Treatment", "Treatment"),
        ("Medication", "Medication"),
        ("Outcome", "Outcome"),
        ("Doctor_Name", "Doctor Name"),
        ("Hospital_Name", "Hospital Name"),
    ]:
        value = row.get(key)
        if value and str(value).strip():
            parts.append(f"{label}: {value}")
    return "\n".join(parts)


def main():
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"Dataset not found at {DATA_FILE}")

    df = pd.read_csv(DATA_FILE)
    documents = []
    texts = []

    for _, row in df.iterrows():
        text = format_document(row)
        if not text.strip():
            continue
        documents.append({"id": row.get("Patient_ID"), "text": text})
        texts.append(text)

    vectorizer = TfidfVectorizer(stop_words="english")
    embeddings = vectorizer.fit_transform(texts).astype(np.float32)

    os.makedirs(VECTOR_DIR, exist_ok=True)
    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer, f)
    with open(DOCS_PATH, "wb") as f:
        pickle.dump(documents, f)
    np.savez_compressed(EMBEDDINGS_PATH, embeddings=embeddings.toarray())

    print("Vector store created successfully.")
    print(f"Vectorizer saved to {VECTORIZER_PATH}")
    print(f"Documents saved to {DOCS_PATH}")
    print(f"Embeddings saved to {EMBEDDINGS_PATH}")


if __name__ == "__main__":
    main()
