import streamlit as st
import requests
import sqlite3

# ? MUST BE FIRST
st.set_page_config(page_title="GeoForge", layout="wide")

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.title("GeoForge")

st.sidebar.markdown("""
### Plan

**Free Tier**
- 5 analyses/day

**Pro (coming soon)**
- unlimited analysis
- multi-model insights
""")

# ---------------------------
# RECENT ANALYSES (SAFE)
# ---------------------------
st.sidebar.subheader("Recent Analyses")

try:
    conn = sqlite3.connect("geoforge.db")
    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT timestamp FROM results ORDER BY id DESC LIMIT 5"
    ).fetchall()

    for r in rows:
        st.sidebar.write(r[0])

except Exception:
    st.sidebar.write("No history yet")

# ---------------------------
# MAIN UI
# ---------------------------
st.title("?? GeoForge")
st.markdown("### AI Citation Intelligence Platform")

col1, col2 = st.columns(2)

with col1:
    target = st.text_input("Target URL", placeholder="https://your-site.com")

with col2:
    competitor = st.text_input("Competitor URL", placeholder="https://competitor.com")

# ---------------------------
# ANALYZE BUTTON
# ---------------------------
if st.button("Analyze", use_container_width=True):

    if not target or not competitor:
        st.error("Please enter both URLs")

    else:
        try:
            with st.spinner("Analyzing AI citation patterns..."):

                response = requests.post(
                    "https://geoforgeai.up.railway.app/analyze",
                    json={
                        "target_url": target,
                        "competitor_url": competitor
                    },
                    headers={"x-api-key": "test-key-123"},
                    timeout=60
                )

            if response.status_code != 200:
                st.error(f"API failed: {response.text}")

            else:
                result = response.json()

                if not result or result.get("data") is None:
                    st.error(f"API Error: {result}")

                else:
                    data = result.get("data", {})

                    # ---------------------------
                    # METRICS
                    # ---------------------------
                    st.subheader("?? Overview")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric("Similarity Score", data.get("similarity_score", "N/A"))

                    with col2:
                        st.metric("Entities Missing", len(data.get("missing_entities", [])))

                    # ---------------------------
                    # INSIGHTS
                    # ---------------------------
                    st.subheader("?? Key Reasons")
                    st.write(data.get("key_reasons", []))

                    st.subheader("?? Missing Entities")
                    st.write(data.get("missing_entities", []))

                    st.subheader("?? Semantic Gaps")
                    st.write(data.get("semantic_gaps", []))

                    st.subheader("?? Recommended Content Sections")
                    st.write(data.get("recommended_sections", ""))

                    st.subheader("?? Model Comparison")
                    st.json(data.get("model_comparison", {}))

        except Exception as e:
            st.error(f"Error connecting to API: {e}")
