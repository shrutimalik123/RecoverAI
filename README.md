# RecoverAI 🏥❤️

**Hackathon Challenge**: ElevenLabs (Voice AI) + Google Cloud (Vertex AI)

## Concept
RecoverAI is a post-discharge monitoring system that bridges the gap between hospital and home. It uses an empathetic, voice-first AI nurse (powered by **ElevenLabs**) to check in on patients, while **Google Vertex AI (Gemini 1.5 Pro)** analyzes their specific discharge summaries to provide accurate, context-aware medical answers.

## 🏗️ Architecture
- **Frontend**: Streamlit (User Interface) - Simple, large-button interface for elderly accessibility.
- **Voice AI**: ElevenLabs Conversational Agent (Web Widget) - Handles speech-to-speech interaction with optimal latency and emotion.
- **Intelligence layer**: Google Vertex AI (Gemini 1.5 Pro) - Processes the patient's "Discharge Summary" to answer specific questions (e.g., "What is my dosage?").
- **Integration**: FastAPI - Acts as the bridge (Tool) between the ElevenLabs Agent and the Vertex AI brain.

## 🚀 Setup & Installation

### 1. Prerequisites
- Google Cloud Project with **Vertex AI API** enabled.
- ElevenLabs Account.
- Python 3.9+ installed.

### 2. Installation
Clone the repo and install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file from the example:
```bash
cp .env.example .env
```
Fill in your credentials:
- `GOOGLE_CLOUD_PROJECT`: Your GCP Project ID.
- `ELEVENLABS_AGENT_ID`: The ID of your configured agent in ElevenLabs.

### 4. Authentication
Ensure your local environment is authenticated with Google Cloud:
```bash
gcloud auth application-default login
```

## 🏃‍♂️ Running the Application

You need to run two components for the full experience:

### 1. The Tool API (Backend)
This allows the ElevenLabs agent to "call" your backend to look up medical info.
```bash
python api.py
```
*Create a tunnel (e.g., ngrok) to expose port 8000 if you need the cloud-hosted ElevenLabs agent to reach your local machine.*

### 2. The Patient Interface
Launch the main app:
```bash
streamlit run app.py
```

## ✅ Progress Log

### Phase 1: Core Implementation
- [x] Project Structure & Dependencies
- [x] Google Vertex AI Integration (`backend.py`) - **Done**
- [x] RAG/Context Logic with Mock Discharge Summary - **Done**
- [x] Streamlit Frontend (`app.py`) - **Done**
- [x] ElevenLabs Widget Embedding - **Done**
- [x] FastAPI Hook for Agent Tools (`api.py`) - **Done**

### Phase 2: Integration & Polish
- [ ] Configure ElevenLabs Agent Tools (Webhooks)
- [ ] End-to-End Testing (Voice -> Tool -> Gemini -> Voice)
- [ ] Demo Video Recording

---
*Built with ❤️ for the Google Cloud AI Hackathon*
