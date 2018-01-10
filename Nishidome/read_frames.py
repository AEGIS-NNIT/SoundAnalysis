# -*- coding: utf-8 -*-
import wave

def main():
    wf = wave.open("planing_idling.wav" , "r" )
    print"Frames:", wf.getnframes()

if __name__ == '__main__':
    main()
    
