#!/usr/bin/env python
import sys

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

if __name__ == "__main__":
	test_ip_addresses = {
		'192.168.1' : False,
		'10.1.1.' : False,
		'10.1.1.x' : False,
		'0.77.22.19' : False,
		'-1.88.99.17' : False,
		'241.17.17.9' : False,
		'127.0.0.1' : False,
		'169.254.1.9' : False,
		'192.256.7.7' : False,
		'192.168.-1.7' : False,
		'10.1.1.256' : False,
		'1.1.1.1' : True,
		'223.255.255.255': True,
		'223.0.0.0' : True,
		'10.200.255.1' : True,
		'192.168.17.1' : True,
    }

	for key in test_ip_addresses.keys():
		result = ip_validation(key)
		value = test_ip_addresses.get(key)
		if result == value:
			print str(result) + ":" + str(value)
			print key + " is correct"
			next
		else:
 			print key + " is incorrect"
 			next
 	sys.exit(0)
else:
	print "IPv4_validation imported"


