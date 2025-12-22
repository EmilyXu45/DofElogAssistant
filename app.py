import streamlit as st
import pandas as pd
from database import create_tables, save_log, get_logs
from logic import generate_reflection

create_tables()

st.title("📘 DofE Log Assistant")

# ---- Session state (prevents refresh problems) ----
if "reflection" not in st.session_state:
    st.session_state.reflection = ""

# ---- Log input ----
st.header("Weekly Log Entry")

week = st.number_input("Week number", min_value=1, max_value=52)
activity = st.text_input("What activity did you do?")
skills = st.text_input("What skills did you develop?")
challenges = st.text_area("What challenges did you face?")

# ---- Generate reflection ----
if st.button("Generate Reflection"):
    st.session_state.reflection = generate_reflection(
        activity, skills, challenges
    )

# ---- Show reflection if exists ----
if st.session_state.reflection:
    st.subheader("Suggested Reflection")
    st.write(st.session_state.reflection)

    if st.button("Save Log"):
        save_log(
            week,
            activity,
            skills,
            challenges,
            st.session_state.reflection
        )
        st.success("✅ Log saved successfully!")
        st.session_state.reflection = ""

# ---- View saved logs ----
st.header("📊 Saved Logs")

logs = get_logs()

if logs:
    df = pd.DataFrame(
        logs,
        columns=[
            "ID", "Week", "Activity", "Skills",
            "Challenges", "Reflection", "Date"
        ]
    )
    st.dataframe(df)
else:
    st.info("No logs saved yet.")
