import sys
import pyaudio

p=pyaudio.PyAudio()
count=p.get_device_count()
devices=[]
for i in range(count):
	devices.append(p.get_device_info_by_index(i))

for i, dev in enumerate(devices):
	print (i, dev['name'])
