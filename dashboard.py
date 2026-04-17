import streamlit as st
import json
import os
from geoforge.core.registry import registry
import geoforge.skills

st.set_page_config(layout="wide")

st.title("🚀 GeoForge GEO Intelligence")

tab1, tab2, tab3 = st.tabs(["Run Analysis", "Tracking", "RAG Insights"])

# ---------------------------
# TAB 1 — RUN
# ---------------------------
with tab1:
    st.header("Run GEO Analysis")

    target = st.text_input("Target URL")
    competitor = st.text_input("Competitor URL")

    if st.button("Analyze"):
        skill = registry.get("citation-gap")()
        result = skill.run(
            target_url=target,
            competitor_url=competitor
        )

        st.json(result.model_dump())

# ---------------------------
# TAB 2 — TRACKING
# ---------------------------
with tab2:
    st.header("Citation Tracking")

    if os.path.exists("tracking.json"):
        with open("tracking.json") as f:
            data = json.load(f)

        st.write(data)
    else:
        st.write("No tracking data yet")

# ---------------------------
# TAB 3 — RAG
# ---------------------------
with tab3:
    st.header("RAG Simulation")

    url = st.text_input("Enter URL")

    if st.button("Simulate RAG"):
        skill = registry.get("rag-simulate")()
        result = skill.run(url=url)

        st.json(result.model_dump())