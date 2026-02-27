# 🚀 Production-Grade LLM Orchestration with LangChain, Google GEMMA, Groq & Ollama LLaMA2

A **production-ready, modular LLM orchestration framework** leveraging **FastAPI**, **LangChain**, and **Streamlit**. This system enables seamless real-time integration of multiple powerful LLMs including **Google GEMMA**, **Groq’s Gemma2**, and **Ollama’s LLaMA2**—ideal for essay and poetry generation use cases in AI-driven applications.This stack is built for AI researchers, backend engineers, and data scientists seeking a production-grade infrastructure that supports seamless interaction with state-of-the-art LLMs.

This project demonstrates the practical usage of multi-agent orchestration, secure API design, and a lightweight frontend—all aligned with enterprise-grade standards, making it perfect for high-performance AI systems in real-world deployments.

---

## 🔍 Key Highlights

- 🧠 **Multi-Model Orchestration**: Simultaneous use of Google GEMMA (Generative AI), Groq's Gemma2, and Ollama's LLaMA2 using LangChain Agents.
- 🚀 **FastAPI Backend**: Fully functional backend to handle inference requests and serve LLM-generated content via REST APIs.
- 🌐 **Streamlit Frontend**: A minimalist and intuitive UI to interact with the backend and generate results in real-time.
- 🔐 **Secure Configuration**: Environment-based API management using `.env` files.
- 📊 **LangChain Tracing v2**: Debugging and performance tracing enabled out-of-the-box.
- 📊 **Speech Recognition**: Enable Voice Input Functionality to the LLMs Models.

---

## 🧠 Real-World Use Cases

- **AI-Powered Content Generation Systems**
- **Creative Writing Tools for Students and Writers**
- **Internal Knowledge Assistants in Enterprises**
- **Multilingual Essay and Poetry Generation Bots**
- **Rapid Prototyping of Multi-Model LLM Solutions**
- **Educational Platforms Enhancing Language Learning**

---

## 📁 Project Structure

```
├── app.py              # FastAPI backend for LLM orchestration
├── client.py           # Streamlit frontend client
├── .env                # Environment variables for API keys
├── requirements.txt    # Python dependencies
├── README.md           # Documentation file
```

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.8+
- `pip` (Python package installer)
- Access to API keys for Google Generative AI, Groq, and Langchain

### Step-by-Step

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/langchain-llm-orchestrator.git
cd langchain-llm-orchestrator
```

2. **Create & Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate   # On Windows
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Set Up Environment Variables**
Create a `.env` file with the following content:
```
LANGCHAIN_API_KEY=your_langchain_api_key
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
```

---

## 🚀 Running the App

### Backend (FastAPI)

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend (Streamlit)

In a new terminal:

```bash
streamlit run client.py
```

---

## 🔗 API Endpoints

| Endpoint     | Method | Description                              |
|--------------|--------|------------------------------------------|
| `/genai`     | POST   | Interacts with Google GEMMA (Generative AI) |
| `/essay`     | POST   | Generates essay using Groq’s Gemma2 model |
| `/poem`      | POST   | Generates poem using Ollama LLaMA2        |

---

## 📦 Dependencies

- fastapi
- uvicorn
- langchain
- langchain_groq
- langchain_google_genai
- langchain_community (Ollama support)
- langserve
- python-dotenv
- streamlit
- requests

---

## 📌 Notes

- The `.env` file is critical for keeping your API keys secure.
- Ensure all API services are enabled and properly authenticated.
- This stack is designed for **local execution**; to deploy it, update the `host`, `CORS`, and networking rules accordingly.

---

## 🪪 License

MIT License

---

## 📬 Contact

Have questions or suggestions? Feel free to reach out at: **garvsharma835@gmail.com**
