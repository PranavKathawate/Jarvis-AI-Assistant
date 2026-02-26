import warnings
warnings.filterwarnings("ignore")

import sounddevice as sd
import numpy as np
import tempfile
import os
from scipy.io.wavfile import write
from core.router import route_command

import whisper


model = whisper.load_model("base")


def start_listening():

    print("Listening for command...")

    fs = 16000
    duration = 5

    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype='int16'
    )

    sd.wait()

    temp_dir = tempfile.gettempdir()

    temp_path = os.path.join(temp_dir, "jarvis_temp.wav")

    write(temp_path, fs, recording)

    text = speech_to_text(temp_path)

    if text:

        print("User said:", text)

        route_command(text)



def speech_to_text(audio_path):

    try:

        result = model.transcribe(
            audio_path,
            fp16=False
        )

        text = result["text"].strip().lower()

        return text

    except:

        return None