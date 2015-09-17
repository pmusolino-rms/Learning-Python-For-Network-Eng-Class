#!/usr/bin/env python


entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"
entries = [entry1,entry2,entry3,entry4]

print "%-20s %-20s" %("ip_prefix","as_path")

for entry in entries:
	bgp_array=entry.split()
	ip_prefix = bgp_array[1]
	as_path = bgp_array[4:-1]
	print "%-20s %-20s" %(ip_prefix,as_path)


exit(0)