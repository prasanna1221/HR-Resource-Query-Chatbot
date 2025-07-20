import streamlit as st

def chat_input_box():
    return st.text_input("💬 Ask your HR query:")

def display_response(response: str):
    st.markdown(response)

def display_employee_list(employees: list):
    st.markdown("### 🔍 Matching Employees")
    for e in employees:
        st.markdown(
            f"**{e['name']}** - {e['experience_years']} yrs - {', '.join(e['skills'])}\n"
            f"_Projects_: {', '.join(e['projects'])} | _Available_: {e['availability'].capitalize()}"
        )
        st.markdown("---")
