#!/usr/bin/env python

from show_version.model import obtain_model
from show_version.os_version import obtain_os_version
from show_version.uptime import obtain_uptime

with open("show_version.txt") as f:
	a = f.read()

model = obtain_model(a)
os = obtain_os_version(a)
uptime = obtain_uptime(a)

print "%-15s: %-15s" %("model",model)
print "%-15s: %-15s" %("os_version",os)
print "%-15s: %-15s" %("uptime",uptime)
