#!/usr/bin/env python

import sys
import re

if __name__ == "__main__":
	pass
else:
	print "Importing %s"  %__file__

	def obtain_uptime(output):
		uptime = re.findall(r"(uptime is .+)",output)
		if uptime:
			return uptime.pop()
		else:
			return None