#!/usr/bin/env python

import re

#Constants for time
MINUTE_SECONDS = 60
HOUR_SECONDS = 60 * MINUTE_SECONDS
DAY_SECONDS = 24 * HOUR_SECONDS
WEEK_SECONDS = 7 * DAY_SECONDS
YEAR_SECONDS = 365 * DAY_SECONDS

class Uptime(object):
	def __init__(self,uptime_string):
		self.years = 0
		self.weeks = 0
		self.days = 0
		self.hours = 0
		self.minutes = 0
		S = ","

		uptime_string = re.search(r"\w uptime is (.*)",uptime_string).group(1)
		uptime_string_split = uptime_string.split(S)

		for time_unit in uptime_string_split:
			time_unit = time_unit.lstrip()
			if "year" in time_unit:
				self.years = int(time_unit.split(" ")[0])
			if "week" in time_unit:
				self.weeks = int(time_unit.split(" ")[0])
			if "day" in time_unit:
				self.days = int(time_unit.split(" ")[0])
			if "hour" in time_unit:
				self.hours = int(time_unit.split(" ")[0])
			if "minute" in time_unit:
				self.minutes = int(time_unit.split(" ")[0])

	def uptime_in_seconds(self):
		seconds = self.years * YEAR_SECONDS
		seconds += self.weeks * WEEK_SECONDS
		seconds += self.days * DAY_SECONDS
		seconds += self.hours * HOUR_SECONDS
		seconds += self.minutes * MINUTE_SECONDS

		return (seconds)