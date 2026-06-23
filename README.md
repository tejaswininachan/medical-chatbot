
# 🩺 Medical Question Answer Chatbot

A **Medical Question Answer Chatbot** built using **Python, Scikit-learn, Pandas, and NumPy**.  
This project uses **local TF-IDF embeddings** to answer **medical-related questions** from a structured medical dataset with semantic search.

---

## 🚀 Features

- Medical Question Answering  
- Local TF-IDF Semantic Search  
- Fast Vector-based Retrieval  
- Console Mode (interactive CLI)  
- Streamlit Web UI (optional)  
- Medical Dataset Support  
- No External API Required  
- Natural Language Output  
- Free and Open Source  

---

## 🛠️ Technologies Used

- Python 3.13+
- Scikit-learn (TF-IDF Vectorizer)
- Pandas (Data Processing)
- NumPy (Vector Operations)
- Streamlit (Optional Web UI)
- Medical Records Dataset (CSV)

---

## 📂 Project Structure

```
Medical-Chatbot/
│
├── Data/
│   └── medical_records_dataset (1).csv
│
├── vector_store/
│   ├── tfidf_vectorizer.pkl
│   ├── documents.pkl
│   └── embeddings.npz
│
├── app.py
├── ingest.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/tejaswininachan/medical-chatbot.git
cd medical-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📊 Build Vector Database

Run the following command to create TF-IDF embeddings from the dataset:

```bash
python ingest.py
```

Expected Output:

```
Vector store created successfully.
Vectorizer saved to vector_store\tfidf_vectorizer.pkl
Documents saved to vector_store\documents.pkl
Embeddings saved to vector_store\embeddings.npz
```

---

## ▶️ Run Application

### Console Mode (Interactive CLI)

```bash
python app.py
```

Output:
```
Medical QA chatbot is running in console mode.
Type a question and press Enter. Press Ctrl+C to exit.

Ask a medical question: What are the symptoms of diabetes?
```

### Streamlit Web UI (Optional)

If you have Streamlit installed:

```bash
streamlit run app.py
```

Application will start at: `http://localhost:8501`

---

## 💬 Example Questions

* What are the symptoms of diabetes?
* What is the treatment for hypertension?
* What medicines are used for asthma?
* What is the diagnosis for kidney disease?
* What is anemia?
* Symptoms of thyroid disorder
* What is the outcome for recovered patients?

---

## 🧠 How It Works

1. **Data Loading**: Medical dataset is loaded from CSV file.
2. **Text Processing**: Patient records are formatted into searchable text.
3. **Vectorization**: Text is converted into TF-IDF embeddings using Scikit-learn.
4. **Storage**: Vectorizer, documents, and embeddings are saved locally.
5. **Query**: User asks a medical question via CLI or web UI.
6. **Search**: Cosine similarity finds top-3 most relevant records.
7. **Response**: Results are formatted and displayed to the user.

---

## ⚠️ Disclaimer

⚕️ **This chatbot is for educational and informational purposes only.**
It does **NOT** provide medical diagnosis or treatment.
Always consult a qualified healthcare professional.

---

## 📈 Future Enhancements

* Disease-wise Filtering
* Patient History Tracking
* Multi-language Support
* Advanced Ranking Models
* Chat History Storage
* Export Results to PDF

---

## 🎯 Learning Outcomes

* Text Vectorization (TF-IDF)
* Cosine Similarity Search
* Pickle Serialization
* NumPy Array Operations
* Data Processing with Pandas
* Streamlit Deployment

---

## 👩‍💻 Author

**Tejaswini Nachan**

GitHub: [https://github.com/tejaswininachan](https://github.com/tejaswininachan)

---

## ⭐ Support

If you found this project useful, please ⭐ star the repository and share it with others.

