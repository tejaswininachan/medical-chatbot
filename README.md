
# 🩺 Medical Question Answer Chatbot

A **Medical Question Answer Chatbot** built using **LangChain, FAISS, Hugging Face, Streamlit, and Sentence Transformers**.  
This project uses **Retrieval-Augmented Generation (RAG)** to answer **medical-related questions** from a structured medical dataset.

---

## 🚀 Features

- Medical Question Answering  
- Retrieval-Augmented Generation (RAG)  
- Semantic Search using FAISS  
- Hugging Face LLM Integration  
- Interactive Streamlit UI  
- Medical Dataset Support  
- Fast and Accurate Responses  
- Natural Language Output  
- Free and Open Source  

---

## 🛠️ Technologies Used

- Python  
- LangChain  
- FAISS Vector Database  
- Hugging Face Inference API  
- Sentence Transformers  
- Streamlit  
- Pandas  
- Medical Records Dataset (CSV)

---

## 📂 Project Structure

```

Medical-Chatbot/
│
├── data/
│   └── medical_records_dataset.csv
│
├── vector_store/
│   └── faiss_index/
│
├── app.py
├── ingest.py
├── requirements.txt
├── .env
└── README.md

````

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/medical-chatbot.git
cd medical-chatbot
````

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

## 🔑 Environment Variables

Create a `.env` file and add your Hugging Face token:

```env
HUGGINGFACEHUB_API_TOKEN=YOUR_HUGGINGFACE_API_TOKEN
```

---

## 📊 Build Vector Database

Run the following command to create FAISS embeddings:

```bash
python ingest.py
```

Expected Output:

```
FAISS Index Created Successfully
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will start at:

```
http://localhost:8501
```

---

## 💬 Example Questions

* What are the symptoms of diabetes?
* What is the treatment for hypertension?
* Common causes of fever
* What medicines are used for asthma?
* Explain heart disease
* Precautions for COVID-19
* What is anemia?
* Symptoms of thyroid disorder

---

## 🧠 How It Works

1. Medical dataset is loaded from CSV file.
2. Data is converted into text embeddings.
3. Embeddings are stored in FAISS vector database.
4. User asks a medical question.
5. Relevant data is retrieved using semantic search.
6. Hugging Face LLM generates a natural language answer.
7. Streamlit displays the response in chat format.

---

## ⚠️ Disclaimer

⚕️ **This chatbot is for educational and informational purposes only.**
It does **NOT** provide medical diagnosis or treatment.
Always consult a qualified healthcare professional.

---

## 📈 Future Enhancements

* Disease-wise Search
* Medicine Recommendation System
* Chat History
* Voice-based Assistant
* Multi-language Support
* Advanced Medical LLM Models

---

## 🎯 Learning Outcomes

* Retrieval-Augmented Generation (RAG)
* Vector Databases (FAISS)
* LangChain Framework
* Semantic Search
* Medical AI Applications
* Streamlit Deployment

---

## 👩‍💻 Author

**Tejaswini Nachan**

GitHub: [https://github.com/tejaswininachan](https://github.com/tejaswininachan)

---

## ⭐ Support

If you found this project useful,
please ⭐ star the repository and share it with others.

Thank You 

