#Python3

import wave

def main():
	wf=wave.open("pyaudio_output_10mm.wav","r")
	print ('Sample Width:',wf.getsampwidth())

if __name__=='__main__':
	main()

