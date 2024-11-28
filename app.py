import gradio as gr
import requests
import os
from utils.azure_speech import request_stt, request_tts

# Environment variables for Azure keys
SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION")
SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")

# Function to handle Speech-to-Text (STT)
def change_audio(file_path):
    if file_path:
        return request_stt(file_path, SPEECH_REGION, SPEECH_KEY)
    else:
        return "No audio file provided."

# Function to handle Text-to-Speech (TTS)
def change_text_to_audio(text):
    if text:
        audio_content = request_tts(text, SPEECH_REGION, SPEECH_KEY)
        if audio_content:
            return audio_content  # Return the generated audio
        else:
            return "TTS Error: Unable to generate audio."
    else:
        return "No text provided."

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Azure AI Speech Processing Platform")

    # Speech-to-Text (STT) Section
    with gr.Column():
        gr.Markdown("### Speech-to-Text (STT)")
        input_mic = gr.Audio(label="Microphone Input", type="filepath", sources="microphone", waveform_options=gr.WaveformOptions(
            waveform_color="#00FFFF",
            waveform_progress_color="#FF00FF",
            skip_length=2,
            show_controls=False
        ))
        output_textbox = gr.Textbox(label="Transcribed Text")
        input_mic.change(fn=change_audio, inputs=[input_mic], outputs=[output_textbox])

    # Text-to-Speech (TTS) Section
    with gr.Column():
        gr.Markdown("### Text-to-Speech (TTS)")
        input_tts_textbox = gr.Textbox(label="Text Input", placeholder="Enter text to convert to speech.")
        output_tts_audio = gr.Audio(label="Generated Audio", interactive=False)
        send_tts_button = gr.Button("Generate Speech")

        # Link TTS processing to button click
        send_tts_button.click(fn=change_text_to_audio, inputs=[input_tts_textbox], outputs=[output_tts_audio])

demo.launch()
