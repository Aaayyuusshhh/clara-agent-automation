import whisper
from pathlib import Path

print("Loading Whisper model...")
model = whisper.load_model("base")

audio_path = Path("data/onboarding_audio/bens_onboarding_call.m4a")

print("Starting transcription...")

result = model.transcribe(str(audio_path))

output_path = Path("data/onboarding_audio/onboarding_transcript.txt")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(result["text"])

print("Transcription completed.")
print(f"Transcript saved at: {output_path}")