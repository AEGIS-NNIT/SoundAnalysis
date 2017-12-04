# This program is written in Python3

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

# create an arthmetical progression
# np.linspace(start, stop, numbers (default = 50), endpoint = "boolian" (default = True))
t = np.linspace(-1, 1, 200, endpoint = False)
# create a Gaussian modulated sinusoid
# signal.gausspulse((array)time, fc = "center frewuency[Hz]")
sig = np.cos(2 * np.pi * 7 * t) + signal.gausspulse(t - 0.4, fc = 2)

# couldn't understand yet
widths = np.arange(1, 31)
#Conitnuous wavelet transform
# signal.cwt(data, wavelet, widths)
# Ricker wavelet a.k.a. Mexican hat wavelet
cwtmatr = signal.cwt(sig, signal.ricker, widths)

# set figure size
# plt.figure(figsize = [width times 100, height times 100])
plt.figure(figsize = [16, 9])
# set interval between two figures
plt.subplots_adjust(hspace=0.25)

# plt.subplot(row, column, order)
plt.subplot(2, 1, 1)
# plot figure
# plt.plot(x-axis, y-axis)
plt.plot(t, sig)
# set title
plt.title("Original Signal")
# set x-label
plt.xlabel("Time")
# set t-label
plt.ylabel("Amplitude")

plt.subplot(2, 1, 2)
plt.imshow(cwtmatr, extent = [-1, 1, 1, 31], cmap = "PRGn", aspect = "auto", vmax = abs(cwtmatr).max(), vmin = -abs(cwtmatr).max())
plt.title("Continuous Wavelet Transform")
plt.xlabel("Time")
plt.ylabel("Frequency")

# save figure
plt.savefig("1.CWT_sample.png")
# standart output figure
plt.show()
