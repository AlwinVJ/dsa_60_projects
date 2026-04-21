import streamlit as st
from dsa.array_ds import StudentArray

if "student_db" not in st.session_state:
    st.session_state.student_db = StudentArray()

db = st.session_state.student_db

def run():
    st.title("Student Record System")
    
    # Add student
    st.subheader('Add Student')
    name = st.text_input("Name")
    roll = st.number_input("Roll No",step = 1)
    
    if st.button("Add Record"):
        db.add_student(name,roll)
        st.success("Student Record Added")
        
    # Show students
    
    st.subheader("All Student")
    st.write(db.get_all())
    
    # Search
    
    st.subheader("Search Student")
    student_roll = st.number_input("Enter the roll number to search",step=1,key="search")
    
    if st.button("Search"):
        result = db.search_students(student_roll)
        if result:
            st.success(result)
        else:
            st.error("Not found")
    
    #Delete student record
    
    st.subheader("Delete Student")
    del_roll = st.number_input("Enter the roll number to be removed",step=1,key="delete")
    
    if st.button("Delete"):
        if db.delete_students(del_roll):
            st.success("Deleted")
        else:
            st.error("Not Found")