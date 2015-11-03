#!/usr/bin/env python

import sys
import re

if __name__ == "__main__":
	pass
else:
	print "Importing %s"  %__file__

	def obtain_os_version(output):
		version = re.findall(r"Cisco IOS Software, .*, (Version .+?),",output)
		if version:
			return version.pop()
		else:
			return None