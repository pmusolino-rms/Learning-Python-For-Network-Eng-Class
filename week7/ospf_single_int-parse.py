#!/usr/env/python

import re

with open("ospf_single_interface.txt") as f:
	a = f.read()

interface = re.search("(.+?) .+line protocol",a).group(1)
ip,area = re.search("Internet Address (.+?), Area (.+?),",a).group(1,2)
net_type = re.search("Network Type (.+?),",a).group(1)
hello,dead = re.search("Hello (.+?), Dead (.+?),",a).group(1,2)
cost = re.search(" .+[0-9] .+([0-9]+)",a).group(1)
print "%-7s %-15s" %("Int:",interface)
print "%-7s %-15s" %("IP:",ip)
print "%-7s %-15s" %("Area:",area)
print "%-7s %-15s" %("Type:",net_type)
print "%-7s %-15s" %("Cost:", cost)
print "%-7s %-15s" %("Hello:",hello)
print "%-7s %-15s" %("Dead:",dead)

exit(0)