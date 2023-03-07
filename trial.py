"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./credential.json"

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
with open("script.txt", "r") as f:
    text = f.read()
    synthesis_input = texttospeech.SynthesisInput(text=text)
# synthesis_input = texttospeech.SynthesisInput(text="おれだよ俺、覚えてない？")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="ja-JP", ssml_gender=texttospeech.SsmlVoiceGender.MALE, name="ja-JP-Neural2-D"
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    effects_profile_id=["small-bluetooth-speaker-class-device"],
    pitch=1.2,
    speaking_rate=1.3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
