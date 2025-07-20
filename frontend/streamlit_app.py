import streamlit as st
import requests
from pathlib import Path

# ────────────────────────────────────────────────
# ✅ Streamlit Page Setup
# ────────────────────────────────────────────────
st.set_page_config(page_title="HR Chatbot", layout="wide")
st.title("🤖 HR Chatbot (RAG + FastAPI)")

# ────────────────────────────────────────────────
# ✅ Load Optional Custom CSS (Optional)
# ────────────────────────────────────────────────
style_path = Path(__file__).parent / "style.css"
if style_path.exists():
    with open(style_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.warning("Custom style.css not found – using default styles.")

# ────────────────────────────────────────────────
# ✅ Text Input
# ────────────────────────────────────────────────
query = st.text_input("💬 Ask your HR query:", placeholder="E.g., Who has React and ML experience?")

# ────────────────────────────────────────────────
# ✅ Handle Query
# ────────────────────────────────────────────────
if query:
    with st.spinner("🔍 Thinking..."):
        try:
            # API Call to FastAPI server
            response = requests.post("http://localhost:8000/chat", json={"question": query}, timeout=10)

            if response.status_code == 200:
                data = response.json()

                if "response" in data:
                    st.success("✅ Answer:")
                    st.markdown(data["response"], unsafe_allow_html=True)
                else:
                    st.error("❌ No 'response' key found in API response.")
                    st.json(data)  # Show full response for debugging
            else:
                st.error(f"❌ API Error {response.status_code}: {response.text}")

        except requests.exceptions.RequestException as e:
            st.error(f"⚠️ Request failed: {str(e)}")
