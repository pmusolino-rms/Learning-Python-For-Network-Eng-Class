#!/usr/bin/env python

import telnetlib
import time

def disable_paging(remote_conn,command="terminal length 0\n", delay=1):

	remote_conn.write("\n")
	remote_conn.write(command)

	time.sleep(delay)
	output = remote_conn.read_very_eager()

	return output


if __name__ == "__main__":

	ip = ""
	username = ""
	password = ''

	TELNET_PORT = 23
	TELNET_TIMEOUT = 6
	READ_TIMEOUT = 6

	remote_conn = telnetlib.Telnet(ip,TELNET_PORT,TELNET_TIMEOUT)

	output = remote_conn.read_until("sername:", READ_TIMEOUT)
	remote_conn.write(username + "\n")

	output = remote_conn.read_until("ssword:", READ_TIMEOUT)
	remote_conn.write(password + "\n")

	time.sleep(1)

	# turn off pager
	output = disable_paging(remote_conn)

	remote_conn.write("sh ver\n")
	time.sleep(1)
	
	output = remote_conn.read_very_eager()

	print output

	remote_conn.close()
