# -*- coding: utf-8 -*-
import wave

def main():
    wf = wave.open("pyaudio_output_200mm.wav" , "r" )
    print"Frames:", wf.getnframes()

if __name__ == '__main__':
    main()
    
