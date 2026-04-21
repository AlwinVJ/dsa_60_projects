import streamlit as st

st.set_page_config(page_title="DSA Systems")

st.sidebar.title("📚 Menu")

page = st.sidebar.radio(
    "Go to",
    ["Home", "Student Record System"]
)

if page == "Home":
    st.title("🚀 DSA Playground")
    st.write("Start with Student Record System")

elif page == "Student Record System":
    from systems.student_array import run
    run()