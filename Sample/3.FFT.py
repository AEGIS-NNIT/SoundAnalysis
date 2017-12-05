from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy as np


Y = abs(fft)

LEN = float(len(Y))

maxim = (LEN - 1)/LEN*fs
dt = fs/LEN
F = np.arange(0, (LEN)/LEN*fs, fs/LEN)
plt.plot(F, Y)
plt.show()
