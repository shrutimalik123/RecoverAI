import os
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models

def init_vertex_ai(project_id, location):
    vertexai.init(project=project_id, location=location)

def get_gemini_response(query: str, context_text: str):
    """
    Queries Gemini with a user question and a provided context (discharge summary).
    """
    model = GenerativeModel("gemini-1.5-pro-001")
    
    prompt = f"""
    You are a medical assistant helper. 
    Use the following Discharge Summary to answer the patient's question.
    If the answer is not in the summary, say "I don't see that in your discharge papers, please verify with your doctor."
    
    Discharge Summary:
    {context_text}
    
    Patient Question:
    {query}
    """
    
    responses = model.generate_content(
        prompt,
        generation_config={
            "max_output_tokens": 2048,
            "temperature": 0.2,
            "top_p": 1
        },
        stream=False,
    )
    
    return responses.text

def mock_get_discharge_summary():
    """
    For the hackathon, we can load a local file or string if GCS is not set up yet.
    """
    return """
    Patient Name: John Doe
    Date of Discharge: 2023-10-25
    Diagnosis: Post-operative Left Knee Replacement
    
    Medications:
    - Amoxicillin 500mg: Take one tablet by mouth every 8 hours for 7 days.
    - Oxycodone 5mg: Take one tablet every 4-6 hours as needed for severe pain. Max 6 tablets per day.
    - Docusate Sodium 100mg: Take one tablet twice daily to prevent constipation.
    
    Instructions:
    - Keep the incision dry and covered for 48 hours.
    - You may shower after 48 hours but do not scrub the incision.
    - Physical Therapy: Start exercises tomorrow, 3 times a day.
    - Follow up with Dr. Smith on Nov 1st at 10:00 AM.
    
    Warning Signs to Call Doctor:
    - Fever above 101 F.
    - Increased redness or drainage from the incision.
    - Calf pain or swelling.
    """
