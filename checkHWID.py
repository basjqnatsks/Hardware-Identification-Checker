import subprocess
import requests
import time
class checkHWID(object):
	def __new__(cls, url=None, debug=0):
		cls.__init__(cls, url, debug)
		return cls.getstatus(cls)
	
	
	def __init__(self, url=None, debug=0):
		self.status = False
		self.hwidstring = str(self.cleanIT(self, self.getHWID(self)))
		self.url = url


		if debug != 0:
			print('Your HWID is ' + self.hwidstring)

		if 'Error' in self.check_server(self).decode('ISO-8859-1'):
			raise PermissionError("Server Issue")

		if self.hwidstring in self.check_server(self).decode('ISO-8859-1'):


			self.status = True
	def getstatus(self):
		return self.status

	def cleanIT(self, string):
		return string.decode('ISO-8859-1').replace('UUID', '').replace(' ', '').replace('\r', '').replace('\n', '')


	
	def getHWID(self):
		proc = subprocess.Popen('wmic csproduct get uuid', stdout=subprocess.PIPE, shell=True)
		(out, err) = proc.communicate()
		return out
	
	
	def check_server(self):
		return requests.get(self.url).content

print(checkHWID('https://www.dropbox.com/s/1rwvfkx2ecyj3xz/host.txt?dl=1', 1))
input()