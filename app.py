import streamlit as st
import os
from dotenv import load_dotenv
from backend import init_vertex_ai, get_gemini_response, mock_get_discharge_summary

# Load environment variables
load_dotenv()

# Initialize Google Cloud
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")
AGENT_ID = os.getenv("ELEVENLABS_AGENT_ID")

if PROJECT_ID:
    init_vertex_ai(PROJECT_ID, LOCATION)

st.set_page_config(page_title="RecoverAI", page_icon="❤️")

# Custom CSS for "wow" factor
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #f0f2f6, #e0e7ff);
    }
    .big-button {
        font-size: 24px !important;
        padding: 20px 40px !important;
        border-radius: 12px !important;
        background-color: #4F46E5 !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.1s;
    }
    .big-button:hover {
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("RecoverAI ❤️")
st.subheader("Your Personal Post-Discharge Assistant")

# Sidebar for debug/context
with st.sidebar:
    st.header("Patient Data")
    discharge_summary = mock_get_discharge_summary()
    st.text_area("Discharge Summary (Context)", value=discharge_summary, height=300)

# Main Interaction Area
col1, col2 = st.columns([1, 1])

with col1:
    st.image("https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=400&q=80", caption="Dr. Rachel", use_column_width=True)

with col2:
    st.markdown("### 🗣️ Speak with your Nurse")
    st.write("Tap the microphone/widget below to start talking.")
    
    if AGENT_ID:
        # Embedding the ElevenLabs Conversational Widget
        # Note: This requires the widget script to be added to the HTML component
        # We can use st.html or st.components.v1.html
        
        widget_code = f"""
        <elevenlabs-convai agent-id="{AGENT_ID}"></elevenlabs-convai>
        <script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
        """
        st.components.v1.html(widget_code, height=300)
    else:
        st.warning("Please configure ELEVENLABS_AGENT_ID in .env")

st.markdown("---")
st.markdown("### or Type your question")

user_query = st.text_input("Ask a question about your medication or recovery:")

if st.button("Ask"):
    if user_query:
        with st.spinner("Consulting your discharge papers..."):
            try:
                # In a real tool-use scenario, the Agent acts as the router.
                # Here we simulate the tool logic directly for text fallback.
                answer = get_gemini_response(user_query, discharge_summary)
                st.success(answer)
            except Exception as e:
                st.error(f"Error: {e}")
                st.info("Make sure you have authenticated with Google Cloud (`gcloud auth application-default login`)")

