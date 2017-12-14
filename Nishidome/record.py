import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK=2**13
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"

audio=pyaudio.PyAudio()

stream=audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,input_device_index=2,frames_per_buffer=CHUNK)

print("* recording")

frames=[]

for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
	try:
		data=stream.read(CHUNK)
	except IOError:
		pass
	frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
audio.terminate()

wf=wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
