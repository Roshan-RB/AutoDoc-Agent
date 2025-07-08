# 🤖 AutoDoc-Agent

An interactive app that analyzes code step-by-step using GPT-4o and LangGraph. It detects the programming language, explains functionality, generates documentation, and inserts inline comments — all in one intelligent pipeline.

---

## ✨ Features

* 🔍 **Language Detection**
* 🧠 **Code Functionality Summary**
* 📄 **Auto-generated Documentation**
* 📝 **Inline Code Commenting**
* 💡 **Streamlit Frontend with Real-time Feedback**
* 🌐 Powered by **LangChain**, **LangGraph**, and **OpenAI GPT-4o**

---

## 📸 Demo

> *Paste code and watch AI explain it live.*
![image](https://github.com/user-attachments/assets/a12d6f3e-54af-4767-add9-c0c9ea25dcef)
![image](https://github.com/user-attachments/assets/8ad346df-df60-449c-a2e9-41765e7ae28f)
![image](https://github.com/user-attachments/assets/8b83e0d8-0836-4bd8-acfc-2b15c5b3bfe8)
![image](https://github.com/user-attachments/assets/a71be4e4-0212-4b39-85fa-9d1ea3209b0e)


---

## 🧪 Example Use

### Input:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

### Output:

* **Language**: Python
* **Functionality**: Computes factorial recursively
* **Inline Comments**: ✅
* **Markdown Docs**: ✅

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/code-understanding-agent.git
cd code-understanding-agent
```

### 2. Create `.env` file

Create a `.env` file and add your OpenAI key:

```
OPENAI_API_KEY=your-key-here
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 🧠 What I Learned

* ✅ Building modular LLM workflows using `LangGraph`
* ✅ Prompt engineering with LangChain's `PromptTemplate`
* ✅ Streaming step-by-step agent execution with `stream()`
* ✅ Reusable node functions for flexible pipeline logic
* ✅ Creating interactive Streamlit dashboards
* ✅ Markdown rendering and inline code annotation

---

## 🛠️ Tech Stack

* [LangChain](https://www.langchain.com/)
* [LangGraph](https://github.com/langchain-ai/langgraph)
* [Streamlit](https://streamlit.io/)
* [OpenAI GPT-4o-mini](https://openai.com/gpt-4o-mini)
* Python 3.10+

---

## 🗂 Project Structure

```bash
📦 code-understanding-agent
┣ 📜 streamlit_app.py         # Streamlit frontend
┣ 📜 agent_file.py            # LangGraph workflow & node logic
┣ 📜 run_agent.py          # Optional CLI testing script
┣ 📜 requirements.txt
┣ 📜 .env.example
┣ 📂 assets/                  # Screenshots / GIFs
```

---

