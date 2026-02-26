import pvporcupine
import pyaudio
import struct

porcupine = pvporcupine.create(
    access_key="Og50EzHdOsYSA2Y3lkjDqnc6T7vRt5993FCYvUeNzKGTRchPQy+hTA==",
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

print("Listening for wake word...")

while True:
    pcm = audio_stream.read(porcupine.frame_length)
    pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
    keyword_index = porcupine.process(pcm)

    if keyword_index >= 0:
        print("Wake word detected")