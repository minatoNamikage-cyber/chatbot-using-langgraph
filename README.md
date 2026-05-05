# 🤖 Chatbot using LangGraph

An intelligent conversational AI chatbot built using **LangGraph** and **LLMs**, designed to handle multi-turn conversations with contextual awareness.

---

## 🚀 Overview

This project demonstrates how to build a **stateful AI chatbot** using LangGraph, a graph-based orchestration framework for LLM applications.
Unlike traditional chatbots, this system maintains conversation flow using a structured graph model.

---

## 🧠 Key Features

* 🔹 Graph-based conversation flow using LangGraph
* 🔹 Context-aware responses (maintains chat history)
* 🔹 Modular architecture (easy to extend)
* 🔹 LLM-powered response generation
* 🔹 Scalable design for future multi-agent systems

---

## 🏗️ Architecture

```
User Input → StateGraph → LLM → Response → Update State
```

### Components:

* **LangGraph** – Controls conversation flow
* **LLM (OpenAI / Gemini)** – Generates responses
* **State Management** – Maintains chat history
* **Python Backend** – Core logic

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/minatoNamikage-cyber/chatbot-using-langgraph.git
cd chatbot-using-langgraph
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup environment variables

Create a `.env` file and add your API key:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Usage

Run the chatbot:

```bash
python backend.py
```

OR (if Streamlit UI is used):

```bash
streamlit run frontend.py
```

---

## 📂 Project Structure

```
chatbot-using-langgraph/
│
├── backend.py          # Core chatbot logic
├── frontend.py         # UI (Streamlit / CLI)
├── requirements.txt    # Dependencies
├── .env                # API keys
└── README.md           # Documentation
```

---

## 🔄 How It Works

1. User provides input
2. Input is passed into LangGraph
3. Graph node processes request
4. LLM generates response
5. State is updated
6. Response is returned

---

## 🚧 Limitations

* ❌ No persistent memory (chat resets on restart)
* ❌ No external tools (search, APIs, etc.)
* ❌ Basic single-node graph implementation
* ❌ Limited UI

---

## 🔮 Future Improvements

* ✅ Add vector database (FAISS / Pinecone)
* ✅ Implement RAG (Retrieval-Augmented Generation)
* ✅ Multi-agent workflows
* ✅ FastAPI backend deployment
* ✅ Authentication & logging

---

## 💡 Use Cases

* AI assistants
* Customer support bots
* Learning assistants
* Research copilots

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Siddharth (Siddu)**

* GitHub: https://github.com/minatoNamikage-cyber
* LinkedIn: https://www.linkedin.com/in/siddharth-s-515a3b310/

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
