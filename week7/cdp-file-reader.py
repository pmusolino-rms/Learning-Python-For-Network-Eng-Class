#!/usr/bin/env python

import re

with open("r1_cdp.txt") as f:
	a = f.read()

hostname = re.search(r"Device ID: (.+)",a).group(1)
ip = re.search(r"IP address: (.+)",a).group(1)
vendor,model = re.search(r"Platform: (.+?) (.+?),",a).group(1,2)
device_type = re.search(r"Platform: .+Capabilities: (.+?) ",a).group(1)

print "%15s: %15s" %("Hostname",hostname)
print "%15s: %15s" %("IP",ip)
print "%15s: %15s" %("Vendor",vendor)
print "%15s: %15s" %("Model",model)
print "%15s: %15s" %("Device Type",device_type)

exit(0)
