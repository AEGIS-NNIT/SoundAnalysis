# -*- coding: utf-8 -*-
import wave
import numpy as np
import matplotlib.pyplot as plt

def main():
    wf = wave.open("pyaudio_output_50mm.wav" , "r" )
    buf = wf.readframes(wf.getnframes())
    # バイナリデータを16bit整数に変換
    data = np.frombuffer(buf, dtype="int16")
    plt.plot(data)
    plt.savefig("Wave_50mm.png")          # グラフ保存

if __name__ == '__main__':
    main()
