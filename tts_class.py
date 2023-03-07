from google.cloud import texttospeech
import os
import numpy as np
import librosa
import soundfile as sf

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./credential.json"


class TTS:
    def __init__(self, lang, gender, speaker_name, pitch, rate):
        if gender == "male":
            ssml_gender = texttospeech.SsmlVoiceGender.MALE
        else:
            ssml_gender = texttospeech.SsmlVoiceGender.FEMALE
        self.voice = texttospeech.VoiceSelectionParams(
            language_code=lang,
            ssml_gender=ssml_gender,
            name=speaker_name
        )
        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            effects_profile_id=["small-bluetooth-speaker-class-device"],
            pitch=pitch,
            speaking_rate=rate
        )
        self.client = texttospeech.TextToSpeechClient()

    def run(self, text, filename, silent=False):
        synthesis_input = texttospeech.SynthesisInput(text=text)

        response = self.client.synthesize_speech(
            input=synthesis_input, voice=self.voice, audio_config=self.audio_config
        )

        with open(filename, "wb") as out:
            out.write(response.audio_content)

        if silent is True:
            y, sr = librosa.load(filename, sr=None)
            silent = np.zeros(int(sr * 1))
            y = np.concatenate([y, silent])
            sf.write(filename, y, sr)
