# vim:fileencoding=utf-8

import time

import numpy as np

import soundfile as sf
import pyaudio as pa


# global
xs = np.array([])


def callback(in_data, frame_count, time_info, status):
    global xs
    in_float = np.frombuffer(in_data, dtype=np.int16).astype(np.float)
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
    chunk = 1024
    use_device_index = 2

    # 入力ストリームを作成
    in_stream = p_in.open(format=py_format,
                          channels=channels,
                          rate=fs,
                          input=True,
                          frames_per_buffer=chunk,
                          input_device_index=use_device_index,
                          stream_callback=callback)

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
    sf.write("./pyaudio_output_200mm.wav", xs, fs)

    p_in.terminate()
