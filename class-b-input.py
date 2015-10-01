#!/usr/bin/env python
S="."

ip_addr = raw_input("Enter a class B Ip address: ")

octets =  ip_addr.rstrip('\n').split(S)

if len(octets) == 3:
	octets.append('0')
elif len(octets) == 4:
	octets[3] = '0'

addr=S.join(octets)

print "IP address: " + addr + "\n"


print "%-20s %-20s %-20s" %("NETWORK_NUMBER","FIRST_OCTET_BINARY","FIRST_OCTET_HEX")
print "%-20s %-20s %-20s" %(addr,oct(int(octets[0])),hex(int(octets[0])))

exit(0)