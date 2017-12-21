# -*- coding: utf-8 -*-
import wave
import numpy as np
import matplotlib.pyplot as plt

# 離散フーリエ変換
def dft (n0, N, g):
    G = [0.0] * N
    for k in range(N):
        for n in range(N):
            real = np.cos(2 * np.pi * k * n / N)
            imag = - np.sin(2 * np.pi * k * n / N)
            G[k] += g[n0 + n] * complex(real, imag)
    return G

def main():
    wf = wave.open("sine.wav" , "r" )
    fs = wf.getframerate()                          # サンプリング周波数
    g = wf.readframes(wf.getnframes())
    g = np.frombuffer(g, dtype= "int16")/32768.0    # -1～1に正規化
    wf.close()
    n0 = 0                                          # サンプリング開始位置
    N = 256                                         # サンプル数
    G = np.fft.fft(g[n0:n0+N])                      # 高速フーリエ変換
    amp = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in G]       # 振幅スペクトル
    phase = [np.arctan2(int(c.imag), int(c.real)) for c in G]   # 位相スペクトル
    f_list = np.fft.fftfreq(N, d=1.0/fs)             # 周波数リスト
    window = np.hamming(N)    # ハミング窓
    #window = np.hanning(N)    # ハニング窓
    #window = np.blackman(N)  # ブラックマン窓
    #window = np.bartlett(N)  # バートレット窓
    G1 = np.fft.fft(g[n0:n0+N])
    G2 = np.fft.fft(window * g[n0:n0+N])
    amp1 = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in G1]
    amp2 = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in G2]
    # 波形サンプルを描画
    plt.subplot(221)
    plt.plot(range(n0, n0+N), g[n0:n0+N])
    plt.axis([n0, n0+N, -1.0, 1.0])
    plt.xlabel("Time [sample]")
    plt.ylabel("Amplitude")

    # 波形サンプルを描画（窓関数あり）
    plt.subplot(222)
    plt.plot(range(n0, n0+N), window * g[n0:n0+N])
    plt.axis([n0, n0+N, -1.0, 1.0])
    plt.xlabel("time [sample]")
    plt.ylabel("Amplitude")

    # 振幅スペクトルを描画
    plt.subplot(223)
    plt.plot(f_list, amp1, marker='o', linestyle='-')
    plt.axis([0, fs/2, 0, 15])
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Amplitude spectrum")

    # 位相スペクトルを描画（窓関数あり）
    plt.subplot(224)
    plt.plot(f_list, amp2, marker='o', linestyle='-')
    plt.axis([0, fs/2, 0, 15])
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Amplitude spectrum")
    plt.show()

if __name__ == '__main__':
    main()
