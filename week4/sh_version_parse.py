#!/usr/bin/env python

import sys
import pprint

VENDOR_OS_STRING="Cisco IOS Software"
MODEL_STRING="bytes of memory"
SERIAL_STRING="Processor board ID"
UPTIME_STRING="uptime"
search_strings = (VENDOR_OS_STRING,MODEL_STRING,SERIAL_STRING,UPTIME_STRING)

sh_version_data = """Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: 
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X

License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices

Configuration register is 0x2102"""

sh_version_data = sh_version_data.lstrip().split("\n")

sh_version_dict ={}

for line in sh_version_data:
	if VENDOR_OS_STRING in line:
		vendor = line.split(',')
		sh_version_dict = {"vendor":vendor[0]}
		sh_version_dict.update({"OS":",".join(vendor[1:])})
	elif (MODEL_STRING in line):
		model = line.split(' ')
		sh_version_dict.update({"model":" ".join(model[0:-5])})
	elif (SERIAL_STRING in line):
		serial = line.split(' ')
		sh_version_dict.update({"serial":serial[-1]})
	elif (UPTIME_STRING in line):
		uptime = line.split(' ')
		sh_version_dict.update({"uptime":" ".join(uptime[3:])})


pprint.pprint(sh_version_dict)

