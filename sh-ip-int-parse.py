#!/usr/bin/env python

show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10          YES     NVRAM       up          up
NVI0                  6.9.4.10          YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''

show_ip_int_brief = show_ip_int_brief.lstrip().split("\n")
show_ip_int_brief.pop()
tuple_list=[]

for i,line in enumerate(show_ip_int_brief):
	if i == 0:
		continue
	fields = line.split()
	if (fields[4] == 'down') or (fields[5]=='down'):
		continue
	else:
		interface_tuple=(fields[0],fields[1],fields[4],fields[5])
    	tuple_list.append(interface_tuple)

print "%-20s %-20s %-20s %-20s" %("Interface","IP Address","Status","Protocol")
for tuples in (tuple_list):
	for fields in tuples:
		print "%-20s" %fields,
	print ""
exit(0)