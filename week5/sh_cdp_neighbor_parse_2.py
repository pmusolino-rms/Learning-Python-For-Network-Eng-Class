#!/usr/bin/env python

import sys
import pprint

sw1_show_cdp_neighbors = '''
SW1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                                 S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone
Device ID            Local Intrfce        Holdtme        Capability        Platform    Port ID
R1                    Fas 0/11              153            R S I           881          Fas 1
R2                    Fas 0/12              123            R S I           881          Fas 1
R3                    Fas 0/13              129            R S I           881          Fas 1
R4                    Fas 0/14              173            R S I           881          Fas 1
R5                    Fas 0/15              144            R S I           881          Fas 1
'''

sw1_show_cdp_neighbors_detail = '''
SW1> show cdp neighbors detail
--------------------------
Device ID: R1
Entry address(es):
   IP address: 10.1.1.1
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/11, Port ID (outgoing port): FastEthernet1
Holdtime: 153 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
--------------------------
Device ID: R2
Entry address(es):
   IP address: 10.1.1.2
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/12, Port ID (outgoing port): FastEthernet1
Holdtime: 123 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
--------------------------
Device ID: R3
Entry address(es):
   IP address: 10.1.1.3
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/13, Port ID (outgoing port): FastEthernet1
Holdtime: 129 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
--------------------------
Device ID: R4
Entry address(es):
   IP address: 10.1.1.4
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/14, Port ID (outgoing port): FastEthernet1
Holdtime: 173 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
--------------------------
Device ID: R5
Entry address(es):
   IP address: 10.1.1.5
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/15, Port ID (outgoing port): FastEthernet1
Holdtime: 144 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
'''

r1_show_cdp_neighbors = '''
R1>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/11
'''

r1_show_cdp_neighbors_detail = '''
R1>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/11
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

r2_show_cdp_neighbors = '''
R2>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/12
'''

r2_show_cdp_neighbors_detail = '''
R2>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/12
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

r3_show_cdp_neighbors = '''
R3>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/13
'''

r3_show_cdp_neighbors_detail = '''
R3>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/13
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

r4_show_cdp_neighbors = '''
R4>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/14
'''

r4_show_cdp_neighbors_detail = '''
R4>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/14
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

r5_show_cdp_neighbors = '''
R5>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/15
'''

r5_show_cdp_neighbors_detail = '''
R5>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/15
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full


'''

network_devices = {}

sw1_cdp = sw1_show_cdp_neighbors.lstrip().rstrip().split("\n")
sw1_cdp = sw1_cdp[4:]

sw1_cdp_detail = sw1_show_cdp_neighbors_detail.lstrip().rstrip().split("\n")
for neighbor_detail in sw1_cdp_detail:
	if "Device ID" in neighbor_detail:
		hostname = neighbor_detail.split()[-1]
		network_devices.update({hostname:{}})
	if "IP address" in neighbor_detail:
		ip = neighbor_detail.split()[-1]
		network_devices[hostname].update({"ip":ip})
		next
	if "Platform" in neighbor_detail:
		vendor,device_type = neighbor_detail.split(",")
		model = vendor.split()[-1]
		vendor = vendor.split()[1]
		device_type = device_type.split()[1]
		network_devices[hostname].update({"vendor":vendor,"device_type":device_type,"model":model})

r1_cdp = r1_show_cdp_neighbors.lstrip().rstrip().split("\n")
r1_cdp = r1_cdp[4:]

r1_cdp_detail = r1_show_cdp_neighbors_detail.lstrip().rstrip().split("\n")
for neighbor_detail in r1_cdp_detail:
	if "Device ID" in neighbor_detail:
		hostname = neighbor_detail.split()[-1]
		network_devices.update({hostname:{}})
	if "IP address" in neighbor_detail:
		ip = neighbor_detail.split()[-1]
		network_devices[hostname].update({"ip":ip})
		next
	if "Platform" in neighbor_detail:
		vendor,device_type = neighbor_detail.split(",")
		model = vendor.split()[-1]
		vendor = vendor.split()[1]
		device_type = device_type.split()[1]
		network_devices[hostname].update({"vendor":vendor,"device_type":device_type,"model":model})
device_neighbor_list = [sw1_show_cdp_neighbors,r1_show_cdp_neighbors,r2_show_cdp_neighbors,r3_show_cdp_neighbors,r4_show_cdp_neighbors,r5_show_cdp_neighbors]

for neighbor_list in device_neighbor_list:
		neighbor_list = neighbor_list.lstrip().rstrip().split("\n")
		hostname = neighbor_list[0].split(">")[0]
		neighbor_list = neighbor_list[4:]
		adjacent_devices = []
		for neighbor in neighbor_list:
			neighbor = neighbor.split()[0]
			adjacent_devices.append(neighbor)
			network_devices[hostname].update({"adjacent_devices":adjacent_devices})
pprint.pprint(network_devices)
