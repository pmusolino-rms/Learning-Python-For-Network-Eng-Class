#!/usr/bin/env python

import sys

S="."
invalid = False
while True:
	ip_addr = raw_input("Enter a valid Ipv4 address: ")
	octets = ip_addr.split(S)

	if len(octets) != 4:
		print ("Invalid IP address.  Please use correct IPv4 formatting\n")
		invalid = True
	else:
		invalid = False

	if invalid:
		next

	for i,octet in enumerate(octets):

		try:
			octet = int(octet)
			invalid = False
		except ValueError:
			print("Invalid IP Address: %s\n" %ip_addr)
			invalid = True

		if invalid:
			break


		if (0 <= octet <= 255):
			if i == 0:
				if (octet == 0):
					print("%s: 'This network' addresses not permitted\n" %ip_addr)
					invalid = True
					break
				elif (octet == 127):
					print("%s: Loopback IPs not permitted\n" %ip_addr)
					invalid = True					
					break
				elif (octet == 169 and int(octets[1]) == 254):
					print("%s: Link Local IPs not permitted\n" %ip_addr)
					invalid = True
					break
				elif ( 224 <= octet <= 239):
					print("%s: Multicast Addresss not permitted\n" %ip_addr)
					invalid = True
					break
				elif (240 <= octet <= 255):
					print("%s: RFC1112 Section 4 IP Space not permitted\n" %ip_addr)
					invalid = True
					break
				else:
					invalid = False
					continue
			else:
				invalid = False
				continue
		else:
			print("%s: IP address out of range\n" %ip_addr)
			invalid = True
			break

	if invalid:
		next
	else:
		break

print "%s is Valid\n" %ip_addr
exit(0)