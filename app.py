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

    # Show table
    st.dataframe(df)

    # =====================================
    # 📈 PROGRESS INSIGHTS (ADD HERE)
    # =====================================
    st.header("📈 Progress Insights")

    # ---- Progress bar ----
    TOTAL_WEEKS = 30
    completed_weeks = df["Week"].nunique()
    progress = completed_weeks / TOTAL_WEEKS

    st.subheader("Overall Progress")
    st.progress(progress)
    st.write(f"Completed **{completed_weeks} / {TOTAL_WEEKS}** weeks")

    # ---- Weekly completion chart ----
    st.subheader("Weekly Log Completion")
    weekly_counts = df.groupby("Week").size()
    st.bar_chart(weekly_counts)

    # ---- Skills frequency chart ----
    st.subheader("Skills Developed")

    all_skills = (
        df["Skills"]
        .str.lower()
        .str.split(",")
        .explode()
        .str.strip()
    )

    skill_counts = all_skills.value_counts()
    st.bar_chart(skill_counts)

else:
    st.info("No logs saved yet.")
