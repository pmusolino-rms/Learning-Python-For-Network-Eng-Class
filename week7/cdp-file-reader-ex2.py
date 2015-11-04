#!/usr/bin/env python

import re
	
def println(name,value):
	print ("%15s: %15s" %(name,value))


def main():
	with open("sw1_cdp.txt") as f:
		a = f.read()

	ips = re.findall(r"IP address: (.+)",a)
	hostnames = re.findall(r"Device ID: (.+)",a)
	platforms = re.findall(r"Platform: (.+?),",a)

	cdp_dict = {}
	cdp_dict.update({"remote_hosts":hostnames})
	cdp_dict.update({"IPs":ips})
	cdp_dict.update({"platform":platforms})

	order = ('remote_hosts','IPs','platform')
	for j in order:
		println(j,cdp_dict[j])
	exit(0)

if __name__ == "__main__":
	main()