#!/usr/bin/env python

import sys
import pprint

#Constants for time
MINUTE_SECONDS = 60
HOUR_SECONDS = 60 * MINUTE_SECONDS
DAY_SECONDS = 24 * HOUR_SECONDS
WEEK_SECONDS = 7 * DAY_SECONDS
YEAR_SECONDS = 365 * DAY_SECONDS

# Instructor provided strings
uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

uptime_list = [uptime1,uptime2,uptime3,uptime4]
uptime_dict = {}

# iterate through each string and split off the first 4 strings, but save the hostname

for i,uptime in enumerate(uptime_list):
	uptime = uptime.split(" ")
	hostname = uptime[0]
	uptime=" ".join(uptime[3:])
	uptime=uptime.split(",")
	uptime_seconds = 0
	# Convert time units into their seconds equivalent and sum it.
	for time_unit in uptime:
		time_unit = time_unit.lstrip()
		if "years" in time_unit:
			time_unit = time_unit.split(" ")
			uptime_seconds += int(time_unit[0]) * YEAR_SECONDS
		if "weeks" in time_unit:
			time_unit = time_unit.split(" ")			
			uptime_seconds += int(time_unit[0]) * WEEK_SECONDS
		if "days" in time_unit:
			time_unit = time_unit.split(" ")			
			uptime_seconds += int(time_unit[0]) * DAY_SECONDS	
		if "hours" in time_unit:
			time_unit = time_unit.split(" ")			
			uptime_seconds += int(time_unit[0]) * HOUR_SECONDS
		if "minutes" in time_unit:
			time_unit = time_unit.split(" ")
			uptime_seconds += int(time_unit[0]) * MINUTE_SECONDS
	#add to dictionary
	uptime_dict.update({hostname:uptime_seconds})
pprint.pprint(uptime_dict)
sys.exit(0)