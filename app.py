import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import plotly.express as px
from config import DB_CONFIG

# 1. Page Configuration (Wide layout)
st.set_page_config(page_title="News Sentiment Dashboard", page_icon="📈", layout="wide")

st.title("📈 Live News Sentiment Dashboard")
st.markdown("Monitor top business news sentiment to gauge the current market mood.")

# 2. Database Connection
url_object = URL.create(
    "mysql+mysqlconnector",
    username=DB_CONFIG['user'],
    password=DB_CONFIG['password'],
    host=DB_CONFIG['host'],
    database="news_db",
)
engine = create_engine(url_object)

# 3. Fetch Data
try:
    df = pd.read_sql("SELECT title, sentiment, saved_at FROM news ORDER BY saved_at DESC", engine)
    
    if df.empty:
        st.warning("No data found! Please run `pipeline.py` first to fetch news.")
    else:
        # Calculate Stats
        total = len(df)
        pos = len(df[df["sentiment"] == "positive"])
        neg = len(df[df["sentiment"] == "negative"])
        neu = len(df[df["sentiment"] == "neutral"])

        # 4. Smart Alerts
        st.markdown("### Market Status")
        if total > 0:
            neg_pct = (neg / total) * 100
            if neg_pct >= 60:
                st.error(f"🚨 ALERT: {neg_pct:.0f}% news is negative! High Market Risk detected.")
            elif pos > neg:
                st.success("🟢 Market mood is generally POSITIVE.")
            else:
                st.warning("🟡 Market mood is slightly negative or mixed.")

        st.markdown("---")

        # 5. KPI Metrics Cards
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total News", total)
        col2.metric("Positive 🟢", pos)
        col3.metric("Negative 🔴", neg)
        col4.metric("Neutral ⚪", neu)

        st.markdown("---")

        # 6. Visualizations using Plotly
        # Count the sentiments for charts
        sentiment_counts = df['sentiment'].value_counts().reset_index()
        sentiment_counts.columns = ['Sentiment', 'Count']
        
        # Color mapping for consistency
        color_map = {'positive': '#28a745', 'negative': '#dc3545', 'neutral': '#6c757d'}

        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.subheader("Sentiment Distribution")
            # Donut Chart
            fig_pie = px.pie(
                sentiment_counts, 
                names='Sentiment', 
                values='Count', 
                color='Sentiment',
                color_discrete_map=color_map,
                hole=0.4 # Makes it a donut chart
            )
            st.plotly_chart(fig_pie, use_container_width=True)

        with chart_col2:
            st.subheader("Sentiment Comparison")
            # Bar Chart
            fig_bar = px.bar(
                sentiment_counts, 
                x='Sentiment', 
                y='Count',
                color='Sentiment',
                color_discrete_map=color_map,
                text='Count'
            )
            fig_bar.update_traces(textposition='outside')
            st.plotly_chart(fig_bar, use_container_width=True)

        st.markdown("---")

        # 7. Interactive Data Table
        st.subheader("📰 Recent Headlines")
        
        # Filter dropdown
        selected_sentiments = st.multiselect(
            "Filter by Sentiment:",
            options=["positive", "negative", "neutral"],
            default=["positive", "negative", "neutral"]
        )
        
        # Apply filter and show dataframe
        filtered_df = df[df['sentiment'].isin(selected_sentiments)]
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)

except Exception as e:
    st.error(f"Database Connection Error. Details: {e}")