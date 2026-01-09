# 📄 Ask My Documents – RAG Chatbot

A beginner-friendly **Retrieval-Augmented Generation (RAG) chatbot** built with Python.  
This project allows users to ask questions about their own documents, and the chatbot answers **only using the document content**, reducing hallucinations.

---

## 🚀 Features

- Load and read local text documents
- Split documents into smaller chunks
- Generate embeddings for semantic understanding
- Store embeddings in a vector database (FAISS)
- Perform semantic search over documents
- Answer questions using retrieved context
- Prevent hallucinations by grounding answers in documents

---

## 🧠 What is RAG?

**Retrieval-Augmented Generation (RAG)** combines:
1. **Retrieval** – searching relevant documents
2. **Generation** – using an LLM to answer based on retrieved information

This approach improves accuracy and reliability compared to using an LLM alone.

---

## 🗂️ Project Structure

AskMyDocuments/

├── documents/

    │── sample.txt # Knowledge source

├── load_docs.py # Document loading & chunking

├── embed_docs.py # Embeddings & vector search

├── rag_chatbot.py # Main chatbot logic

├── requirements.txt # Dependencies


---

## ⚙️ Technologies Used

- **Python**
- **FAISS** – vector database for similarity search
- **SentenceTransformers** – text embeddings
- **Google Gemini API** – response generation
- **RAG architecture**

---

## 🔁 How It Works (Pipeline)

User Question

↓

Convert question to embedding

↓

Search document embeddings (FAISS)

↓

Retrieve top relevant chunks

↓

Send context + question to LLM

↓

Generate grounded answer

---

## 🧪 Example Usage

```text
You: What does RAG stand for?
Bot: RAG stands for Retrieval Augmented Generation. 
```
---


## ▶️ How to Run the Project:

1️⃣ Clone the repository

git clone https://github.com/yourusername/ask-my-documents-rag.git

cd ask-my-documents-rag

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Add your API key

In rag_chatbot.py:

genai.configure(api_key="YOUR_API_KEY")

4️⃣ Run the chatbot

python rag_chatbot.py

### 📌 Notes

- This project uses traditional RAG, not agentic RAG

- Only .txt files are supported (PDF support can be added later)

- Chunk size and top-k retrieval can be adjusted

### 🎯 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)

- Embeddings & semantic search

- Vector databases (FAISS)

- Prompt engineering

- Hallucination control

- Modular Python project structure

### 🔮 Future Improvements

- PDF document support

- Agentic RAG with tool calling

- Document editing via AI

- Web-based UI (Streamlit / FastAPI)

- Memory and conversation history

---


## 📁 Extra files you should add (HIGHLY recommended)

### 1️⃣ `requirements.txt`

```txt
faiss-cpu
sentence-transformers
google-generativeai

