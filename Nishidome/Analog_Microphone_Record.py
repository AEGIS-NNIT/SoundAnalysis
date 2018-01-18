from datetime import datetime
from csv import writer
from gpiozero import MCP3008
import pandas as pd
import matplotlib.pyplot as plt

logfile = "test.csv"
looptime = 10000

f = open(logfile, "a")

writer = writer(f)
writer.writerow(["Time", "Value"])

for var in range(0, looptime):
	record_time = datetime.now()
	voltage0 = 3.3 * MCP3008(channel = 0).value
	writer.writerow([record_time, voltage0])
	print(record_time,voltage0)
f.close()

data = pd.read_csv(logfile, parse_dates=[0])

plt.figure(figsize=(16,9))
plt.plot(data.Time, data.Value)
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.savefig("graph.png")
