#!/usr/bin/env python

import sys

S="."
if len(sys.argv) != 2:
	sys.exit("Usage: %s <ip_address>" % sys.argv[0])

ip_addr = sys.argv.pop()
bin_addr = []
octets =  ip_addr.rstrip('\n').split(S)

#print "%-20s %-20s %-20s %-20s" %("first_octet","second_octet","third_octet","fourth octet")

for i in range(len(octets)):
	binary_octet=bin(int(octets[i]))[2:]
	bin_addr.append(binary_octet.zfill(8))
bin_addr= S.join(bin_addr)

print "%-20s %-35s" %("IP Address","Binary")
print "%-20s %-35s" %(ip_addr, bin_addr)

exit(0)