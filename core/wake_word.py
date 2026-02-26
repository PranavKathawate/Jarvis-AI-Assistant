import pvporcupine
import pyaudio
import struct
import time

from core.listener import start_listening


# Your Picovoice Access Key
ACCESS_KEY = "Og50EzHdOsYSA2Y3lkjDqnc6T7vRt5993FCYvUeNzKGTRchPQy+hTA=="


def start_wake_word():

    porcupine = pvporcupine.create(
        access_key=ACCESS_KEY,
        keywords=["jarvis"]
    )

    pa = pyaudio.PyAudio()

    print("Wake word system active...")

    while True:

        # Open mic
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        while True:

            pcm = audio_stream.read(
                porcupine.frame_length,
                exception_on_overflow=False
            )

            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:

                print("Wake word detected")

                # CLOSE mic before listening
                audio_stream.stop_stream()
                audio_stream.close()

                time.sleep(0.5)

                # Listen to command
                start_listening()

                time.sleep(0.5)

                # break to reopen mic cleanly
                break
def detect_wake_word_only():

    porcupine = pvporcupine.create(
        access_key=ACCESS_KEY,
        keywords=["jarvis"]
    )

    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    pcm = audio_stream.read(
        porcupine.frame_length,
        exception_on_overflow=False
    )

    pcm = struct.unpack_from(
        "h" * porcupine.frame_length,
        pcm
    )

    keyword_index = porcupine.process(pcm)

    audio_stream.stop_stream()
    audio_stream.close()
    pa.terminate()

    return keyword_index >= 0