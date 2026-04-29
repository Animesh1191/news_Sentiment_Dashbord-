import requests
import mysql.connector
from datetime import datetime
from config import NEWS_API_KEY, DB_CONFIG

POSITIVE = ["growth", "profit", "win", "rise", "success", "boost", "good", "best", "gain", "up", "positive", "recover", "improve", "launch", "strong"]
NEGATIVE = ["crash", "loss", "fail", "drop", "crisis", "risk", "bad", "worst", "down", "negative", "cut", "layoff", "attack", "war", "death", "danger", "fall"]

def get_sentiment(text):
    if not text:   #agr text me data empty aayega to return neutral aayega
        return "neutral"
    text = text.lower()  #ye bta raha hai agr text me data capital me hai to lower me kardena 
    pos = sum(1 for w in POSITIVE if w in text)  #ye sum kar rha hai kitne positive words mile 
    neg = sum(1 for w in NEGATIVE if w in text)  #ye sum kar rha hai kitne negative words mile
    if pos > neg:   return "positive"            #yenha pe ham check kar rahe kya positive negative se jyada value store kar rha hai kya 
    if neg > pos:   return "negative"            
    return "neutral"                            #agr positive and negative dono hi equal huwe to return neutral aayega

def fetch_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {"apiKey": NEWS_API_KEY, "category": "business", "language": "en", "pageSize": 20}
    res = requests.get(url, params=params)
    return res.json().get("articles", [])

def save_to_db(articles):
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS news_db")
    cur.execute("USE news_db")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id        INT AUTO_INCREMENT PRIMARY KEY,
            title     VARCHAR(300),
            sentiment VARCHAR(20),
            saved_at  DATETIME
        )
    """)
    for a in articles:
        title = a.get("title") or ""
        sentiment = get_sentiment(title)
        cur.execute(
            "INSERT INTO news (title, sentiment, saved_at) VALUES (%s, %s, %s)",
            (title, sentiment, datetime.now())
        )
        print(f"[{sentiment.upper():8}] {title[:70]}")
    conn.commit()
    cur.close()
    conn.close()
    print("\nSab MySQL mein save ho gaya!")

if __name__ == "__main__":
    articles = fetch_news()
    save_to_db(articles)
