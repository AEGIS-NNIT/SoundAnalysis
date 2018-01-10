# -*- coding: utf-8 -*-
import wave

def main():
    wf = wave.open("planing.wav" , "r" )
    print"Frames:", float(wf.getnframes())

if __name__ == '__main__':
    main()
    
