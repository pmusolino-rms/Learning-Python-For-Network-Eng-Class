#!/usr/bin/env python

class IPAddress(object):
	def __init__(self, ip):
		self.ip_addr = ip
		self.S="."

	def dec_to_bin(self):
		bin_addr = []
		octets =  self.ip_addr.rstrip('\n').split(self.S)

		for i in range(len(octets)):
			binary_octet=bin(int(octets[i]))[2:]
			bin_addr.append(binary_octet.zfill(8))
		bin_addr= self.S.join(bin_addr)
		return bin_addr

	def dec_to_hex(self):
		hex_addr = []
		octets =  self.ip_addr.rstrip('\n').split(self.S)

		for i in range(len(octets)):
			hex_octet=hex(int(octets[i]))[2:]
			hex_addr.append(hex_octet.zfill(2))
		hex_addr= self.S.join(hex_addr)
		return hex_addr

	def is_valid(self):
		
		octets = self.ip_addr.split(self.S)

		if len(octets) != 4:
			return False	
		else:
			next
		
		for i,octet in enumerate(octets):

			try:
				octet = int(octet)
			except ValueError:
				return False

			if (0 <= octet <= 255):
				if i == 0:
					if (octet == 0):
						return False
					elif (octet == 127):
						return False				
					elif (octet == 169 and int(octets[1]) == 254):
						return False
					elif ( 224 <= octet <= 255):
						return False
					else:
						continue
				else:
					continue
			else:
				return False
		return True