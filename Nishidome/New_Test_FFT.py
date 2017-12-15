#!/usr/bin/env python
# vim:fileencoding=utf-8

import sys

import numpy as np
import scipy.fftpack as fft
import matplotlib.pyplot as plt

import soundfile as sf

if __name__ == '__main__':
    plt.close("all")

    # wavファイル読み込み
    filename = sys.argv[1]
    wav, fs = sf.read("pyaudio_output.wav")

    # ステレオ2chの場合、LchとRchに分割
    wav_l = wav[:, 0]
    wav_r = wav[:, 1]

    # 入力をモノラル化
    xs = (0.5 * wav_l) + (0.5 * wav_r)

    n_len = len(xs)
    n_fft = 128
    n_overlap = 2
    n_shift = n_fft / n_overlap

    # 中間バッファ
    zs = np.zeros(n_len)
    Zs = np.zeros(n_fft)

    # 出力バッファ
    ys = np.zeros(n_len)

    # 窓関数
    window = np.hanning(n_fft)

    # FFT & IFFT
    for start in range(0, n_len - n_shift, n_shift):
        xs_cut = xs[start: start + n_fft]
        xs_win = xs_cut * window
        Xs = fft.fft(xs_win, n_fft)

        # some signal processing
        Zs = Xs
        zs = fft.ifft(Zs, n_fft)

        # write output buffer
        ys[start: start + n_fft] += np.real(zs)

    # 冒頭から10秒分プロット
    fig = plt.figure(1, figsize=(8, 10))
    ax = fig.add_subplot(211)
    ax.plot(xs[:fs*10])
    ax.set_title("input signal")
    ax.set_xlabel("time [pt]")
    ax.set_ylabel("amplitude")

    ax = fig.add_subplot(212)
    ax.plot(ys[:fs*10])
    ax.set_title("output signal")
    ax.set_xlabel("time [pt]")
    ax.set_ylabel("amplitude")

    plt.savefig("New_Test_FFT.png")
