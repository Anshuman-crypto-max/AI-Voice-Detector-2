from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import librosa
import numpy as np
import io

app = FastAPI(title="AI Voice Detector API")

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SUPPORTED_LANGUAGES = ["English", "Hindi", "Tamil", "Telugu", "Malayalam"]

@app.get("/")
def home():
    return {
        "message": "AI Voice Detection API running",
        "supported_languages": SUPPORTED_LANGUAGES
    }

def extract_features(audio_bytes: bytes):
    try:
        audio_stream = io.BytesIO(audio_bytes)
        y, sr = librosa.load(audio_stream, sr=None)

        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        features = np.mean(mfcc, axis=1)

        return features

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Audio processing failed: {e}")

@app.post("/detect")
async def detect_voice(
    audio: UploadFile = File(...),
    language: str = "English"
):
    if language not in SUPPORTED_LANGUAGES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported language. Choose from {SUPPORTED_LANGUAGES}"
        )

    if not audio.filename.lower().endswith((".mp3", ".wav", ".flac")):
        raise HTTPException(status_code=400, detail="Invalid audio format")

    audio_bytes = await audio.read()
    features = extract_features(audio_bytes)

    # 🔥 Dummy logic (replace with ML model later)
    confidence = round(float(np.random.uniform(0.7, 0.95)), 2)
    classification = "AI Generated Voice" if confidence > 0.85 else "Human Voice"

    return {
        "filename": audio.filename,
        "language": language,
        "classification": classification,
        "confidence_score": confidence
    }
