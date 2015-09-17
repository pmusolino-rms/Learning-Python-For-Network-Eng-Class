#!/usr/bin/env python

import fileinput
S=":"

for line in fileinput.input():
	hexgroups =  line.rstrip('\n').split(S)
	print "Split: " + str(hexgroups)
recombined = S.join(hexgroups)
print "Recombined: " + recombined + "\n"
exit(1)
