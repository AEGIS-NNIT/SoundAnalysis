# This program is written in Python3
# developer : Masazumi Katoh
# coding : UTF-8
# Last Update : 2018/2/15

# to use wav file
import wave
# to use numpy function
import numpy as np
# to use fft library
import scipy.fftpack
# to get datetime
from datetime import datetime
# to record the sound
import pyaudio
import wave
# to sleep
from time import sleep
import csv

# threshold
do = 1010
so = 780

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 11020
CHUNK=2**13
RECORD_SECONDS = 2
time = datetime.now().strftime("%Y%m%d_%H:%M:%S")
WAVE_OUTPUT_FILENAME = "wav/" + time + ".wav"

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

# open wav file
wf = wave.open(WAVE_OUTPUT_FILENAME, "r")
fs = wf.getframerate()
x = wf.readframes(wf.getnframes())
x = np.frombuffer(x, dtype= "int16")
wf.close()
LENGTH = len(x)

# FFT
X = scipy.fftpack.fft(x)
freqList = scipy.fftpack.fftfreq(LENGTH, d=1.0/fs)
Amp = [np.sqrt(c.real ** 2 + c.imag ** 2)/LENGTH for c in X]

# detect peak frequency
peak_index = np.where(Amp == max(Amp))[0][0]
peak_freq = freqList[peak_index]
print(peak_freq)

csv.writer(open("test.csv",'a')).writerow([peak_freq])


# m4a wav transfer
# https://qiita.com/peroon/items/a1673913127fcdbb2338

# np.where
# https://deepage.net/features/numpy-where.html
