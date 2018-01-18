# -*- coding: utf-8 -*-
import wave
import numpy as np
import matplotlib.pyplot as plt

def main():
    wf = wave.open("pyaudio_output_10mm.wav" , "r" ) #読みだしモードでwavファイルを開く
    buf = wf.readframes(wf.getnframes())        #getnframes=wavファイルのオーディオフレーム(サンプリングレート)の総数(サンプリング数)を取得
                                                #readframes=取得したオーディオフレームの総数分だけのデータを取得し、bitesオブジェクトとして返す
    data = np.frombuffer(buf, dtype="int16")    #バイナリデータを16bit整数に変換
                                                #bufのデータを高速に読み込んで1次元配列に格納
    plt.plot(data)                              #描画
    plt.xlabel("Time(プロット数)")
    plt.ylabel("Amplitude()")
    plt.savefig("Wave_10mm.png")               #グラフ保存

if __name__ == '__main__':
    main()
