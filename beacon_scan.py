from bluepy.btle import Scanner, DefaultDelegate
import pandas as pd

class ScanDelegate(DefaultDelegate):
	def __init__(self):
		DefaultDelegate.__init__(self)

	def handleDiscovery(self, dev, isNewDev, isNewData):
		if isNewDev:
			print("Discovered device", dev.addr)
		elif isNewData:
			print("Received new data from", dev.addr)

while(True):
	scanner = Scanner().withDelegate(ScanDelegate())
	devices = scanner.scan(5.0)

	dict = {}
#	try :
	for dev in devices:
		dict[dev.addr] = dev.rssi
		print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
	for (adtype, desc, value) in dev.getScanData():
		print("  %s = %s" % (desc, value))

	file = open('data.html', 'w+')
	df = pd.DataFrame.from_dict(dict, orient='index')
	df = df.sort_values(0)
	data = df.to_html()
	file.write(data)
	file.close()
#	except:
#		print('no device found!')
