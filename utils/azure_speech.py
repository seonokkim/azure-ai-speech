from utils.azure_speech import request_stt, request_tts

# Replace these with actual values or load from your environment
region = "eastus"
key = "your-azure-api-key"

# Test STT
file_path = "path/to/audio.wav"
print("Testing STT...")
print(request_stt(file_path, region, key))

# Test TTS
text = "Hello, this is a test for Text-to-Speech."
print("Testing TTS...")
audio_content = request_tts(text, region, key)
if audio_content:
    with open("output.mp3", "wb") as f:
        f.write(audio_content)
        print("TTS audio saved as 'output.mp3'")
else:
    print("TTS failed.")
