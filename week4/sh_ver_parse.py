#!/usr/bin/python

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4 ac, RELEASE SOFTWARE (fc1)"

show_version = cisco_ios.split(",")
version_number = show_version[2].split("Version ")[1]
print "IOS Version: " + version_number