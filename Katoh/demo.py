# This program is written in Python3

import wave
import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt
import math

sound=input()

wf = wave.open("data_piano/" + sound + ".wav", "r")
fs = wf.getframerate()
x = wf.readframes(wf.getnframes())
x = np.frombuffer(x, dtype= "int16")
wf.close()

LENGTH = len(x)

X = scipy.fftpack.fft(x)

freqList = scipy.fftpack.fftfreq(LENGTH, d=1.0/fs)

Amp = [np.sqrt(c.real ** 2 + c.imag ** 2)/LENGTH for c in X]

maxfreq = np.where(Amp == max(Amp))
peakfreq = maxfreq[0][0]
print(freqList[peakfreq])
# print(maxfreq)

plt.figure(figsize = (16,9), dpi=100)

plt.subplot(211)
plt.plot(x)
plt.title(sound)
plt.xlabel("time [sample]")
plt.ylabel("amplitude")

plt.subplot(212)
plt.plot(freqList, Amp)
# plt.axis([0, 2000, 0, 1000])
plt.xlabel("frequency [Hz]")
plt.ylabel("amplitude")

plt.savefig("FFT/" + sound)
