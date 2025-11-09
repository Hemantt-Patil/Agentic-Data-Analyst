# 📊 Agentic Data Analyst

An **AI-powered data analysis system** using multiple autonomous agents to analyze CSV/Excel data, detect trends, summarize insights, and visualize patterns.

---

## 🧩 Tech Stack

| Layer | Technology |
|--------|-------------|
| **Frontend** | Next.js (TypeScript + TailwindCSS) |
| **Backend** | FastAPI (Python 3.12.6) |
| **Agents** | Insight, Summary, and Visualization Agents |
| **Visualization** | Matplotlib + WordCloud |

---

## ⚙️ Backend Setup

```bash```
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

## 💻 Frontend Setup
cd frontend
npm install
npm run dev

## 🤖 Agent Overview

| Agent                | Role                                         |
| -------------------- | -------------------------------------------- |
| **Insight Agent**    | Finds data trends, outliers, correlations    |
| **Summary Agent**    | Generates human-readable summary             |
| **Visualizer Agent** | Creates visualizations (charts + wordclouds) |

