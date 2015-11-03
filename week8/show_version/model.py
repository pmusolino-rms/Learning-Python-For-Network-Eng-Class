#!/usr/bin/env python

import sys
import re

if __name__ == "__main__":
	pass
else:
	print "Importing %s"  %__file__

	def obtain_model(output):
		model = re.findall(r"Cisco (.+?) .* bytes of memory.",output)
		if model:
			return model.pop()
		else:
			return None