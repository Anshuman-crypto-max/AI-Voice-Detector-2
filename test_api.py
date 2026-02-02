from pathlib import Path
import sys

# CORRECT path for your exact folder structure
script_path = Path(__file__).resolve()
backend_folder = script_path.parent  # ai_voice_detector_backend
project_root = backend_folder.parent  # AI VOICE DETECTOR
audio_path = project_root / "your-audio.file.mp3"

print(f"🔍 Backend folder: {backend_folder}")
print(f"🔍 Project root: {project_root}")
print(f"🔍 Looking for audio: {audio_path}")

# Verify file exists
if not audio_path.exists():
    print("❌ File not found!")
    print("Files in project root:")
    for f in project_root.iterdir():
        print(f"  📁 {f.name}")
    sys.exit(1)

# Load audio
with open(audio_path, "rb") as file:
    audio_data = file.read()
    print(f"✅ SUCCESS! Loaded {len(audio_data):,} bytes")
    print("🎵 Audio file ready for backend.py!")

