from fastapi import FastAPI, Request
from backend import get_gemini_response, mock_get_discharge_summary
import uvicorn
import os

app = FastAPI()

# This is the tool we will register in ElevenLabs
# Tool Description: "Get information from the patient's discharge summary. Use this to answer questions about medications, recovery instructions, or appointments."
# Argument: "query" (string) - The user's specific question.

@app.post("/recover-ai-tool")
async def get_medical_advice(request: Request):
    """
    Webhook for ElevenLabs Agent.
    ElevenLabs sends a POST request with the function arguments.
    """
    data = await request.json()
    print(f"Received Tool Call: {data}")
    
    # Depending on how you configure the tool in ElevenLabs, the payload might differ.
    # Usually, if you define a tool 'get_medical_advice' with argument 'query',
    # the body might look like { "query": "..." } or similar wrapper.
    # For this hackathon, we'll assume a direct JSON body matching the arguments.
    
    user_query = data.get("query")
    if not user_query:
        # Fallback if the structure is different (e.g. conversational wrap)
        # Often it is just the flat arguments.
        return {"response": "I didn't hear a specific question."}

    # Get context
    context = mock_get_discharge_summary()
    
    # Query Gemini
    answer = get_gemini_response(user_query, context)
    
    print(f"Gemini Answer: {answer}")
    
    # Return the result as text for the Agent to speak
    return {"message": answer}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
