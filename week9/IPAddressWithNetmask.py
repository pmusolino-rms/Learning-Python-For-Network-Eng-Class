#!/usr/bin/env python

from IPAddress import IPAddress
import re

class IPAddressWithNetmask(IPAddress):
	def __init__(self,ip_with_netmask):
		ip_addr,self.netmask=re.search(r"(.*)(\/\d+)",ip_with_netmask).group(1,2)
		IPAddress.__init__(self,ip_addr)

	def netmask_in_dotdecimal(self):
		netmask=int(self.netmask.split('/').pop(-1))
		mask = []
		for i in range(netmask):
			mask.append("1")
		for i in range(32 - netmask):
			mask.append("0")
		bin_mask=str.join("",mask)
		first_octet=bin_mask[0:8]
		second_octet=bin_mask[8:16]
		third_octet=bin_mask[16:24]
		fourth_octet=bin_mask[24:32]
		dotdecimal_octets =[]
		dotdecimal_octets.append(str(int(first_octet,2)))
		dotdecimal_octets.append(str(int(second_octet,2)))
		dotdecimal_octets.append(str(int(third_octet,2)))
		dotdecimal_octets.append(str(int(fourth_octet,2)))
		dotdecimal = str.join(self.S,dotdecimal_octets)
		return dotdecimal
