#Python3

import wave

def main():
	wf=wave.open("pyaudio_output.wav","r")
	print ('Frame rate:',wf.getframerate())

if __name__=='__main__':
	main()

