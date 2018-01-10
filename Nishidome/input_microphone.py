# vim:fileencoding=utf-8

import time

import numpy as np

import soundfile as sf
import pyaudio as pa


xs = np.array([])   #変数をnumpy arrayオブジェクトで指定


def callback(in_data, frame_count, time_info, status):
    global xs
    in_float = np.frombuffer(in_data, dtype=np.int16).astype(np.float)
    #np.frombuffer=in_dataを読み込み、16bit整数に変換して返す
    #astype(np.float)=float(浮動小数点)型の
    in_float[in_float > 0.0] /= float(2**15 - 1)
    in_float[in_float <= 0.0] /= float(2**15)
    xs = np.r_[xs, in_float]

    return (in_data, pa.paContinue)

if __name__ == "__main__":
    # pyaudio
    p_in = pa.PyAudio()
    py_format = p_in.get_format_from_width(2)
    fs = 16000
    channels = 1
    chunk = 1024    #音源から1回読み込むときのデータサイズ(個数)。1024(=2の10乗)とする場合が多い。
    #データの書き込みに必要な(録音に掛かる)時間は、chunk/fs=0.064sec
    use_device_index = 2

    # 入力ストリームを作成
    in_stream = p_in.open(format=py_format,     #サンプリングサイズとフォーマット
                          channels=channels,    #チャンネル数
                          rate=fs,              #サンプルレート
                          input=True,
                          frames_per_buffer=chunk,  #バッファごとのフレーム数(バイナリデータの個数)を指定、ここでは1024フレーム
                          input_device_index=use_device_index,  #使用する入力デバイスのインデックスを指定
                          stream_callback=callback)　#コールバック操作のコールバック関数を指定

    in_stream.start_stream()

    # input loop
    # 何か入力したら終了
    while in_stream.is_active():
        c = input()
        if c:
            break
        time.sleep(0.1)
    else:
        in_stream.stop_stream()
        in_stream.close()

    # 入力信号を保存
    sf.write("./pyaudio_output_10mm.wav", xs, fs)

    p_in.terminate()
