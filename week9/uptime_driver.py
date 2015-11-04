#!/usr/bin/env python

import sys
from DeviceUptime import Uptime

if __name__ == "__main__":
	uptime_strings = ['twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes',
		'3750RJ uptime is 1 hour, 29 minutes',
		'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes',
		'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes',
	]

	for uptime in uptime_strings:
		print uptime
		a = Uptime(uptime)
		print "%d years" %a.years
		print "%d weeks" %a.weeks
		print "%d days" %a.days
		print "%d hours" %a.hours
		print "%d minutes" %a.minutes
		print "%d seconds" %a.uptime_in_seconds()

	sys.exit(0)