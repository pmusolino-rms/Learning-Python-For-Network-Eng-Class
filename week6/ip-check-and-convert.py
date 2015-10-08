#!/usr/bin/env python

from ipconverter import dec_to_bin
from  ipv4_validation import ip_validation

while True:
	ip_addr = raw_input("Enter a valid Ipv4 address: ")
	if not ip_validation(ip_addr):
		print "Invalid IP"
		next
	else:
		bin_addr = dec_to_bin(ip_addr)
		print bin_addr
		break
exit(0)
