import streamlit as st
import pandas as pd
from database import get_logs, delete_log

st.title("📊 Progress Dashboard")

logs = get_logs()

if not logs:
    st.info("No logs available yet.")
    st.stop()

df = pd.DataFrame(
    logs,
    columns=[
        "ID", "Week", "Activity", "Skills",
        "Challenges", "Reflection", "Date"
    ]
)


st.subheader("Logs Completed Over Time")

logs_per_week = df.groupby("Week").count()["ID"]
st.bar_chart(logs_per_week)

st.divider()
st.subheader("🗑️ Delete a Log Entry")

log_ids = df["ID"].tolist()

selected_id = st.selectbox(
    "Select a log to delete:",
    log_ids
)

if st.button("Delete selected log"):
    delete_log(selected_id)
    st.success("Log deleted successfully.")
    st.experimental_rerun()

st.subheader("Skills Developed")

skills_series = df["Skills"].str.split(",").explode().str.strip()
skills_count = skills_series.value_counts()

st.bar_chart(skills_count)

