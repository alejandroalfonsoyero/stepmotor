import parallel

class ParallelPortController:
	def __init__(self):
		self.port = parallel.Parallel()

	def setData0(self, value):
		if value is True:
			self.port.setData(self.port.getData() | 0x80)
		else:
			self.port.setData(self.port.getData() & 0x7f)

	def getData0(self):
		return self.port.getData() & 0x80 != 0x00

	def setData1(self, value):
		if value is True:
			self.port.setData(self.port.getData() | 0x40)
		else:
			self.port.setData(self.port.getData() & 0xbf)

	def getData1(self):
		return self.port.getData() & 0x40 != 0x00

	def setData2(self, value):
		if value is True:
			self.port.setData(self.port.getData() | 0x20)
		else:
			self.port.setData(self.port.getData() & 0xdf)

	def getData2(self):
		return self.port.getData() & 0x20 != 0x00

	def setData3(self, value):
		if value is True:
			self.port.setData(self.port.getData() | 0x10)
		else:
			self.port.setData(self.port.getData() & 0xef)

	def getData3(self):
		return self.port.getData() & 0x10 != 0x00

	def setData4(self, value):
		if value is True:
			self.port.setData(self.port.getData() | 0x08)
		else:
			self.port.setData(self.port.getData() & 0xf7)

	def getData4(self):
		return self.port.getData() & 0x08 != 0x00

	def setData5(self, value):
		if value is True:
			self.port.setData(self.port.getData() | 0x04)
		else:
			self.port.setData(self.port.getData() & 0xfb)

	def getData5(self):
		return self.port.getData() & 0x04 != 0x00

	def setData6(self, value):
		if value is True:
			self.port.setData(self.port.getData() | 0x02)
		else:
			self.port.setData(self.port.getData() & 0xfd)

	def getData6(self):
		return self.port.getData() & 0x02 != 0x00

	def setData7(self, value):
		if value is True:
			self.port.setData(self.port.getData() | 0x01)
		else:
			self.port.setData(self.port.getData() & 0xfe)

	def getData7(self):
		return self.port.getData() & 0x01 != 0x00

	def setDataPin(self, dataPin, value):
		if value is True:
			if dataPin == 0:
				self.port.setData(self.port.getData() | 0x80)
			elif dataPin == 1:
				self.port.setData(self.port.getData() | 0x40)
			elif dataPin == 2:
				self.port.setData(self.port.getData() | 0x20)
			elif dataPin == 3:
				self.port.setData(self.port.getData() | 0x10)
			elif dataPin == 4:
				self.port.setData(self.port.getData() | 0x08)
			elif dataPin == 5:
				self.port.setData(self.port.getData() | 0x04)
			elif dataPin == 6:
				self.port.setData(self.port.getData() | 0x02)
			elif dataPin == 7:
				self.port.setData(self.port.getData() | 0x01)
		else:
			if dataPin == 0:
				self.port.setData(self.port.getData() & 0x7f)
			elif dataPin == 1:
				self.port.setData(self.port.getData() & 0xbf)
			elif dataPin == 2:
				self.port.setData(self.port.getData() & 0xdf)
			elif dataPin == 3:
				self.port.setData(self.port.getData() & 0xef)
			elif dataPin == 4:
				self.port.setData(self.port.getData() & 0xf7)
			elif dataPin == 5:
				self.port.setData(self.port.getData() & 0xfb)
			elif dataPin == 6:
				self.port.setData(self.port.getData() & 0xfd)
			elif dataPin == 7:
				self.port.setData(self.port.getData() & 0xfe)

	def getDataPin(self, dataPin):
		if dataPin == 0:
			return self.port.getData() & 0x80 != 0x00
		elif dataPin == 1:
			return self.port.getData() & 0x40 != 0x00
		elif dataPin == 2:
			return self.port.getData() & 0x20 != 0x00
		elif dataPin == 3:
			return self.port.getData() & 0x10 != 0x00
		elif dataPin == 4:
			return self.port.getData() & 0x08 != 0x00
		elif dataPin == 5:
			return self.port.getData() & 0x04 != 0x00
		elif dataPin == 6:
			return self.port.getData() & 0x02 != 0x00
		elif dataPin == 7:
			return self.port.getData() & 0x01 != 0x00
