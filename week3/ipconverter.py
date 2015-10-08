#!/usr/bin/env python

def dec_to_bin(ip_addr):
	S="."
	bin_addr = []
	octets =  ip_addr.rstrip('\n').split(S)

	for i in range(len(octets)):
		binary_octet=bin(int(octets[i]))[2:]
		bin_addr.append(binary_octet.zfill(8))
	bin_addr= S.join(bin_addr)
	return bin_addr