#!/usr/bin/env python

def ip_validation(ip_address):
	S="."
	octets = ip_address.split(S)

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

print "IPv4_validation imported"