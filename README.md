# 📈 Live News Sentiment Dashboard

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![Plotly](https://img.shields.io/badge/Charts-Plotly-purple)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🚀 Overview

This project is a **real-time News Sentiment Analysis Dashboard**.

It automatically:

* Fetches latest business news
* Analyzes sentiment (positive / negative / neutral)
* Stores data in a database
* Displays insights in an interactive dashboard

👉 **Simple meaning:**
It tells you the **current market mood based on news headlines.**

---

## 📸 Screenshots

### 🖥️ Dashboard View

![Dashboard](./screenshots/dashboard.png)

### 📊 Sentiment Charts

![Charts](./screenshots/charts.png)

### 🔍 Filtered Data Table

![Table](./screenshots/table.png)

---

## ✨ Key Features

* 🤖 Fetches live business news using API
* 🧠 Keyword-based sentiment analysis
* 💾 Stores data in MySQL database
* 📊 Interactive charts (Donut + Bar)
* 🎯 KPI summary (total, positive, negative, neutral)
* 🚨 Smart alert if negative news > 60%
* 🔍 Filter news by sentiment

---

## 🧠 How It Works

```text
News API → pipeline.py → MySQL → app.py → Dashboard
```

---

## 📁 Project Structure

```bash
News-Sentiment-Dashboard/
│
├── config.py        # API key + DB config
├── pipeline.py      # Fetch + analyze + store data
├── app.py           # Dashboard UI
├── requirements.txt
└── screenshots/
```

---

## ⚙️ Tech Stack

* Python
* MySQL
* Streamlit
* Pandas
* Requests
* Plotly

---

## 🛠️ Configuration (config.py)

This file stores:

* API key for fetching news
* Database credentials

```python
NEWS_API_KEY = "your_api_key"

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password'
}
```

---

## 🔬 Core Logic Explained

### 🟢 1. Sentiment Analysis Logic

The system uses **keyword matching**:

* Positive words → growth, profit, success, gain
* Negative words → crash, loss, drop, crisis

```python
if pos > neg:
    return "positive"
elif neg > pos:
    return "negative"
else:
    return "neutral"
```

👉 Example:

* "Company reports huge profit" → **positive**
* "Market crash expected" → **negative**

---

### 🔵 2. Fetching News (API Call)

```python
requests.get("https://newsapi.org/v2/top-headlines")
```

* Fetches top 20 business headlines
* Language: English
* Category: Business

---

### 🟠 3. Database Storage

Automatically:

* Creates database → `news_db`
* Creates table → `news`

Table structure:

```sql
id | title | sentiment | saved_at
```

---

### 🟣 4. Data Pipeline (pipeline.py)

This file:

1. Fetches news
2. Calculates sentiment
3. Saves data in MySQL

```bash
python pipeline.py
```

---

### 🔴 5. Dashboard (app.py)

This file:

* Reads data from database
* Shows charts and KPIs
* Displays alerts

```bash
streamlit run app.py
```

---

## ▶️ How to Run

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Run pipeline

```bash
python pipeline.py
```

---

### 3️⃣ Run dashboard

```bash
streamlit run app.py
```

---

## 📊 Example Output

### Sentiment Output in Terminal

```text
[POSITIVE] Company reports strong growth in Q2
[NEGATIVE] Market crash causes investor panic
[NEUTRAL ] New product launched by company
```

---

## 🚨 Smart Alert Logic

If:

```text
Negative News > 60%
```

👉 Dashboard shows:

* ⚠️ High Market Risk Alert

---

## 🔮 Future Improvements

* 🤖 Advanced NLP (VADER / TextBlob)
* ⏱️ Auto-fetch news (scheduler)
* 🔐 Use `.env` for security
* 📈 Historical sentiment trends
* 🌐 Cloud database support

---

## 📜 License

MIT License

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 📢 Share it

---

💡 *A practical project to learn APIs, databases, and real-time dashboards.*
