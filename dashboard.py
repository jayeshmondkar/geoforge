import streamlit as st
import requests
import sqlite3
import pandas as pd

st.set_page_config(page_title="GeoForge", layout="wide")

st.title("🚀 GeoForge — AI Visibility SaaS")

# INPUT
col1, col2 = st.columns(2)

with col1:
    target = st.text_input("Target URL")

with col2:
    competitor = st.text_input("Competitor URL")

topic = st.text_input("Topic")

# RUN
if st.button("Analyze"):

    res = requests.post(
        "http://127.0.0.1:8000/analyze",
        json={
            "target_url": target,
            "competitor_url": competitor,
            "topic": topic
        },
        headers={"x-api-key": "test-key-123"}
    )

    data = res.json()["data"]
    summary = data["summary"]

    st.subheader("📊 Visibility Score")
    st.metric("Score", f"{summary['visibility_score']}%")

    st.progress(summary["visibility_score"] / 100)

    st.subheader("🧠 Query Results")

    for q in data["queries"]:
        st.write(q["query"])
        st.write(q["result"]["answer"])

# ---------------------------
# HISTORY CHART
# ---------------------------
st.subheader("📈 Visibility Trend")

try:
    conn = sqlite3.connect("geoforge.db")
    df = pd.read_sql("SELECT * FROM history", conn)

    if not df.empty:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        st.line_chart(df.set_index("timestamp")["score"])
except:
    st.info("No history yet")