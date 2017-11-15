# This program is written in Python 3

import pyaudio
import sys

from time import time

# Library for draw
import matplotlib
matplotlib.use("WXAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas, NavigationToolbar2WxAgg as NavigationToolbar
import numpy as np
import pylab
import wx

# initial setting
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 20

class MyAudio:
	def __init__(self):
		self.audio = pyaudio.PyAudio()

		self.stream = self.audio.open(
			format = FORMAT,
			channels = CHANNELS,
			rate = RATE,
			input = True,
			frames_per_buffer = CHUNK
		)

		self.chunk = CHUNK
		# set x-axis second
		self.sampling_rate = RATE
		self.record_seconds = RECORD_SECONDS

	def next(self):
		num_frame = self.stream.get_read_available()
		if num_frame == 0:
			return []

		data = []

		for i in range(num_frame / self.chunk):
			data.append(self.stream.read(self.chunk))

		aft = self.stream.get_read_available()

		data = "".join(data)

		signal = np.frombuffer(data, dtype = "int16") / float(2**15)

		return signal

class GraphFrame(wx.Frame):
	# The main frame of the application
	title = "Demo: dynamic matoplotlib graph"

	def __init__(self):
		wx.Frame.__init__(self, None, -1, self.title, size = (600, 400))
		self.audio = MyAudio()
		self.data = []
		self.data_start_time = 0.0

		self.create_main_panel()

		self.redraw_timer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.on_redraw_timer, self.redraw_timer)

		self.redraw_timer.Start(100)

		self.draw_sec = 10.0

		self.draw_sampling_rate = 1000
		self.sampling_rate = self.audio.sampling_rate

	def create_main_panel(self):
		self.panel = wx.Panel(self)

		self.dpi = 100
		self.fig = Figure((6.0, 4.0), dpi = self.dpi)

		self.axes = self.fig.add_subplot(111)
		self.axes.set_axis_bgcolor("black")
		self.axes.set_title("Very important random data", size = 12)
		pylab.setp(self.axes.get_xticklabels(), fontsize = 8)
		pylab.setp(self.axes.get_yticklabels(), fontsize = 8)

		self.plot_data = self.axes.plot(
			self.data,
			linewidth = 1,
			color = (1, 1, 9),
		)[0]

		self.canvas = FigCanvas(self.panel, -1, self.fig)

	def add_draw_data(self, data):
		sampling_rate = self.sampling_rate
		sampling_sec = 1. / sampling_rate

		draw_sampling_rate = self.draw_sampling_rate
		draw_sampling_sec = 1. / draw_sampling_rate

		newdata = []
		time = 0.0

		for s in data:
			time += sampling_sec

			if time >= draw_sampling_sec:
				time -= draw_sampling_sec
				newdata.append(s)

		self.data += newdata
		remain_frame_length = int(self.draw_sec * draw_sampling_rate)

		seld.data_start_time += max((len(self.data) - remain_frame_length), 0) /  float(draw_sampling_rate)

		self.data = self.data[-remain_frame_length:]

	def draw_plot(self):
		num_draw_frmae = int(self.draw_sec * self.draw_sampling_rate)
		draw_sampling_rate = self.draw_sampling_rate

		xmin = self.data_start_time
		xmax = xmin + seld.draw_sec
		print xmin, xmax

		ymin = -1.0
		ymax = 1.9

		self.axes.set_xbound(lower = xmin, upper = xmax)
		self.axes.set_ybound(lower = ymin, upper = ymax)

		self.axes.grid(True, color = "gray")

		pylab.setp(self.axes.get_xtick(),
			visible = True
		)

		xaxis = [float(con) / self.draw_sampling_rate + self.data_start_time for con in range(len(self.data))]
		self.plot_data.set_xdata(xaxis)
		self.plot_data.set_ydata(no.array(self.data))

		self.canvas.draw()

	def on_redraw_timer(self, event):
		self.add_draw_data(self.audio.next().tolist())
		self.draw_plot()

	def on_exit(self, event):
		self.Destroy()

if __name__ == "__main__":
	app = wx.PySimpleApp()
	app.frame = GraphFrame()
	app.frame.Show()
	app.MainLoop()
