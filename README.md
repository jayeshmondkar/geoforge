[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org)

# 🚀 GeoForge

**Open-source GEO (Generative Engine Optimization) toolkit**
Understand how AI systems (ChatGPT, Claude, Perplexity) choose what to cite.

---

## 🧠 Why GeoForge?

Search is changing.

Users no longer click links—they ask AI.

👉 The question is no longer:
**“Do you rank on Google?”**

👉 It’s:
**“Does AI mention you?”**

GeoForge helps you:

* 🔍 Analyze why competitors get cited
* 🧠 Understand AI content preferences
* 📊 Simulate RAG (retrieval behavior)
* ⏱ Track visibility over time

---

## 🔥 Features

* 🤖 AI-powered citation analysis
* 🔁 Multi-prompt GEO testing
* 📦 RAG chunk simulation
* 📊 Citation tracking
* 🕵️ Competitor monitoring
* 🖥 Streamlit dashboard

---

## ⚡ 2-Minute Setup

### 1. Clone

```bash
git clone https://github.com/YOUR_USERNAME/geoforge.git
cd geoforge
```

---

### 2. Setup

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
pip install -e .
```

---

### 3. Add API key

Create `.env`:

```env
OPENAI_API_KEY=your_key_here
```

---

### 4. Run dashboard

```bash
streamlit run dashboard.py
```

---

## 🎥 Demo (Try This)

Enter:

* Target → https://www.yourwebsiteurl.com
* Competitor → https://www.competitorwebsiteurl.com

Click **Analyze**

👉 You’ll see:

* Why competitor is preferred
* Content gaps
* GEO recommendations

---

## 🧪 CLI Example

```bash
geoforge run citation-gap \
  -p target_url=https://example.com \
  -p competitor_url=https://competitor.com
```

---

## 📊 Example Output

```json
{
  "analysis": "Competitor provides clearer structured answers...",
  "recommendations": [
    "Add concise definitions",
    "Improve heading structure",
    "Increase factual density"
  ]
}
```

---

## 🧠 How It Works

GeoForge combines:

* LLM analysis
* content extraction
* RAG simulation
* vector embeddings (optional)

---

## 🛠 Roadmap

* [ ] multi-model testing (Claude, GPT, Gemini)
* [ ] citation ranking tracker
* [ ] SaaS dashboard
* [ ] team collaboration

---

## 🤝 Contributing

PRs welcome.

---

## ⭐ If this helps you, please star the repo

---
