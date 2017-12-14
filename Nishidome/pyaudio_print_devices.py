#Python3

import pyaudio as pa

if __name__=="__main__":
	p_in=pa.PyAudio()
	print "device num: {0}".format(p_in.get_device_count())
	for i in range(p_in.get_device_count()):
		print p_in.get_device_info_by_index(i)

