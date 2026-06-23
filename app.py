import os
import pickle
import sys
from typing import List

import importlib
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

try:
    st = importlib.import_module("streamlit")
    STREAMLIT_AVAILABLE = True
except ModuleNotFoundError:
    st = None
    STREAMLIT_AVAILABLE = False

VECTOR_DIR = os.path.join("vector_store")
VECTORIZER_PATH = os.path.join(VECTOR_DIR, "tfidf_vectorizer.pkl")
DOCS_PATH = os.path.join(VECTOR_DIR, "documents.pkl")
EMBEDDINGS_PATH = os.path.join(VECTOR_DIR, "embeddings.npz")


def load_vector_store():
    if not os.path.exists(VECTORIZER_PATH) or not os.path.exists(DOCS_PATH) or not os.path.exists(EMBEDDINGS_PATH):
        raise FileNotFoundError("Vector store not found. Run ingest.py first to create vector_store.")

    with open(VECTORIZER_PATH, "rb") as f:
        vectorizer = pickle.load(f)
    with open(DOCS_PATH, "rb") as f:
        documents = pickle.load(f)
    embeddings = np.load(EMBEDDINGS_PATH)["embeddings"]
    return vectorizer, documents, embeddings


def build_answer(question: str, hits: List[dict]) -> str:
    if not hits:
        return "No relevant medical records found. Try another question."

    answer_lines = [f"Top {len(hits)} results for: '{question}'\n"]
    for idx, hit in enumerate(hits, start=1):
        answer_lines.append(f"Result {idx}:")
        answer_lines.append(hit["text"])
        answer_lines.append(f"Score: {hit['score']:.4f}\n")
    return "\n".join(answer_lines)


def find_matches(question: str, vectorizer, embeddings: np.ndarray, documents: List[dict], k: int = 3):
    query_vec = vectorizer.transform([question])
    scores = cosine_similarity(query_vec, embeddings).flatten()
    top_idx = np.argsort(scores)[::-1][:k]
    results = []
    for idx in top_idx:
        score = float(scores[idx])
        if score <= 0:
            continue
        results.append({"score": score, "text": documents[idx]["text"]})
    return results


def run_console_mode():
    try:
        vectorizer, documents, embeddings = load_vector_store()
    except FileNotFoundError as exc:
        print(exc)
        print("Run ingest.py first to create the vector store.")
        sys.exit(1)

    print("Medical QA chatbot is running in console mode.")
    print("Type a question and press Enter. Press Ctrl+C to exit.\n")

    while True:
        try:
            question = input("Ask a medical question: ")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

        if not question.strip():
            continue

        hits = find_matches(question, vectorizer, embeddings, documents, k=3)
        print("\n" + build_answer(question, hits) + "\n")


if __name__ == "__main__":
    if not STREAMLIT_AVAILABLE:
        run_console_mode()
    else:
        try:
            vectorizer, documents, embeddings = load_vector_store()
        except FileNotFoundError as exc:
            st.error(str(exc))
            st.stop()

        st.set_page_config(page_title="Medical Chatbot", page_icon="🩺")
        st.title("🩺 Medical Chatbot")
        question = st.text_input("Ask a medical question")
        if question:
            hits = find_matches(question, vectorizer, embeddings, documents, k=3)
            answer = build_answer(question, hits)
            st.text_area("Answer", answer, height=300)
