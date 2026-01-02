import streamlit as st
import pandas as pd
from database import create_tables, save_log, get_logs, delete_log
from logic import generate_reflection

create_tables()

st.title("📘 DofE Log Assistant")


if "reflection" not in st.session_state:
    st.session_state.reflection = ""

st.header("Weekly Log Entry")

week = st.number_input("Week number", min_value=1, max_value=52)
activity = st.text_input("What activity did you do?")
skills = st.text_input("What skills did you develop?")
challenges = st.text_area("What challenges did you face?")



st.subheader("Reflection Style")

reflection_style = st.radio(
    "Choose how you'd like your reflection written:",
    [
        "Structured (What / So what / Now what)",
        "Short & simple",
        "Reflective & personal",
        "Assessor-focused summary"
    ]
)

if st.button("Generate Reflection"):
  st.session_state.reflection = generate_reflection(
    activity,
    skills,
    challenges,
    reflection_style
)



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
if logs:
    st.divider()
    st.subheader("🗑️ Delete a Log")

    log_ids = df["ID"].tolist()

    selected_log_id = st.selectbox(
        "Select a log to delete",
        log_ids,
        key="delete_log_main"
    )

    confirm = st.checkbox(
        "I understand this action cannot be undone",
        key="confirm_delete_main"
    )

    if st.button("Delete selected log"):
        if confirm:
            delete_log(selected_log_id)
            st.success("Log deleted successfully.")
            st.experimental_rerun()
        else:
            st.warning("Please confirm before deleting.")

    st.dataframe(df)

 