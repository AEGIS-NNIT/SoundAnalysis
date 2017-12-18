# -*- coding: utf-8 -*-
import wave
import numpy as np
import matplotlib.pyplot as plt

def main():
    wf = wave.open("pyaudio_output_200mm.wav" , "r" ) #読みだしモードでwavファイルを開く
    buf = wf.readframes(wf.getnframes())        #wavファイルのオーディオフレーム(サンプリングレート)を取得
                                                #取得したオーディオフレームを読み込んで、bitesオブジェクトとして返す
    data = np.frombuffer(buf, dtype="int16")    #バイナリデータを16bit整数に変換
                                                #bufのデータを高速に読み込んで1次元配列に格納
    plt.plot(data)                              #描画
    plt.savefig("Wave_200mm.png")               #グラフ保存

if __name__ == '__main__':
    main()
