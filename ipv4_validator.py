#!/usr/bin/env python

import sys

S="."
if len(sys.argv) != 2:
	sys.exit("Usage: %s <ip_address>" % sys.argv[0])

ip_addr = sys.argv.pop()
octets = ip_addr.split(".")
if len(octets) != 4:
	sys.exit("Invalid IP address.  Please use correct IPv4 formatting\n")

for i,octet in enumerate(octets):
	octet = int(octet)
	if (0 <= octet <= 255):
		if i == 0:
			if (octet == 0):
				sys.exit("%s: 'This network' addresses not permitted\n" %ip_addr)
			elif (octet == 127):
				sys.exit("%s: Loopback IPs not permitted\n" %ip_addr)
			elif (octet == 169 and int(octets[1]) == 254):
				sys.exit("%s: Link Local IPs not permitted\n" %ip_addr)
			elif ( 224 <= octet <= 239):
				sys.exit("%s: Multicast Addresss not permitted\n" %ip_addr)
			elif (240 <= octet <= 255):
				sys.exit("%s: RFC1112 Section 4 IP Space not permitted\n" %ip_addr)
	else:
		sys.exit("%s: IP address out of range" %ip_addr)
print "%s is Valid\n" %ip_addr
exit(0)

