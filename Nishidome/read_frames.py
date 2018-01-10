# -*- coding: utf-8 -*-
import wave

def main():
    wf = wave.open("planing.wav" , "r" )
    print"Time[s]:", float(wf.getnframes()) / wf.getframerate()

if __name__ == '__main__':
    main()
    
