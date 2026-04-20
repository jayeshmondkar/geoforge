import streamlit as st
from geoforge.skills.citation_gap import CitationGapSkill

st.set_page_config(page_title="GeoForge", layout="wide")

st.title("🚀 GeoForge — AI Visibility Platform")

target = st.text_input("Target URL")
competitor = st.text_input("Competitor URL")
topic = st.text_input("Topic")

if st.button("Analyze"):

    if not target or not competitor:
        st.error("Please enter both URLs")
        st.stop()

    with st.spinner("Running AI analysis..."):

        skill = CitationGapSkill()

        data = skill.execute(
            target_url=target,
            competitor_url=competitor,
            topic=topic
        )

        summary = data["summary"]

        st.subheader("📊 Visibility Score")
        st.metric("Score", f"{summary['visibility_score']}%")

        st.progress(summary["visibility_score"] / 100)

        st.subheader("🧠 Query Results")

        for q in data["queries"]:
            st.markdown(f"### 🔍 {q['query']}")
            st.write(q["result"]["answer"])