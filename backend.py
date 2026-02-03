from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# 1. ALLOW CROSS-ORIGIN REQUESTS
# This stops the "CORS" error in your browser console.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.post("/detect")
async def detect_voice(
    audio: UploadFile = File(...),  # Matches formData.append("audio", ...)
    language: str = Form(...)       # Matches formData.append("language", ...)
):
    # This is a placeholder for your AI logic.
    # It will now receive the file and language without the 422 error.
    
    # Simulating a "gaandfaad" high-precision result
    is_ai = random.choice([True, False])
    classification = "AI GENERATED (DEEPFAKE)" if is_ai else "HUMAN AUTHENTIC"
    confidence = round(random.uniform(0.95, 0.99), 4)

    return {
        "classification": classification,
        "confidence_score": confidence
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)