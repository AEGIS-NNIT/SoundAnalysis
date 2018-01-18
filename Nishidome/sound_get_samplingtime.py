#Python3

import wave

def main():
	wf=wave.open("pyaudio_output_10mm.wav","r")
	print ('Frame rate:',wf.getframerate())	#Frame rate = Sampling rate

if __name__=='__main__':
	main()

