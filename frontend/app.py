import streamlit as st
import requests

# Load custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🤖 HR Resource Query Chatbot")

query = st.text_input("Enter your HR query:")

if query:
    print("User query:", query)
    with st.spinner("Searching..."):
        response = requests.post("http://localhost:8000/chat", json={"question": query})
        st.markdown(response.json()["response"])
