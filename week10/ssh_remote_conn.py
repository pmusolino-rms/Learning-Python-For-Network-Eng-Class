#!/usr/bin/env python

import paramiko
import time
import re
import pickle
from DeviceUptime import Uptime

class NetworkDevice(object):
	def __init__(self,ip,username,password):
		self.hostname = None
		self.ip = ip
		self.username = username
		self.password = password
		self.device_type = None
		self.vendor = None
		self.model = None
		self.os_version = None
		self.uptime = None
		self.serial_number = None

	def parse_version_info(self,info):
		self.hostname = self.obtain_hostname(info)
		self.uptime = Uptime(self.obtain_uptime(info)).uptime_in_seconds()
		self.model = self.obtain_model(info)
		self.os_version = self.obtain_os_version(info)
		self.serial_number = self.obtain_serial(info)
		self.vendor = self.obtain_vendor(info)
		self.device_type = self.obtain_device_type()

	def obtain_model(self,output):
		model = re.findall(r"isco (.+?) .* bytes of memory",output)
		if model:
			return model.pop()
		else:
			return None

	def obtain_device_type(self):
		if ('WS' in self.model):
			return "Switch"
		else:
			return None

	def obtain_vendor(self,output):
		vendor = re.findall(r"(.+?) .* bytes of memory.",output)
		if vendor:
			return vendor.pop()
		else:
			return None			

	def obtain_os_version(self,output):
		version = re.findall(r"Cisco IOS Software, .*, (Version .+?),",output)
		if version:
			return version.pop()
		else:
			return None

	def obtain_uptime(self,output):
		uptime = re.findall(r"(.+ uptime is .+)",output)
		if uptime:
			return uptime.pop()
		else:
			return None

	def obtain_hostname(self,output):
		hostname = re.findall(r"(.+) uptime is .+",output)
		if hostname:
			return hostname.pop()
		else:
			return None				

	def obtain_serial(self,output):
		serial = re.findall(r"Processor board ID (.+)",output)
		if serial:
			return serial.pop()
		else:
			return None		
		
	def device_print(self):
		print "hostname: %s" %self.hostname
		print "ip: %s" %self.ip
		print "vendor: %s" %self.vendor
		print "model: %s" %self.model
		print "os: %s" %self.os_version
		print "type: %s" %self.device_type
		print "serial: %s" %self.serial_number
		print "user: %s" %self.username
		#print "pass %s" %self.password
		print "Uptime %s" %self.uptime

def disable_paging(remote_conn,command="terminal length 0\n", delay=1):

	remote_conn.send("\n")
	remote_conn.send("terminal length 0\n")

	time.sleep(delay)
	output = remote_conn.recv(65535)

	return output

def connection_setup(conn,ip,username,password):
	conn.set_missing_host_key_policy(
		paramiko.AutoAddPolicy())
	
	conn.connect(ip,username=username,password=password)
	remote_conn = conn.invoke_shell()

	return remote_conn

if __name__ == "__main__":

	ip = ""
	username = ""
	password = ''
	remote_conn_pre = paramiko.SSHClient()
	ssh_session = connection_setup(remote_conn_pre,ip,username,password)

	# turn off pager
	output = disable_paging(ssh_session)
	ssh_session.send("sh ver\n")

	#wait for command
	time.sleep(1)
	output = ssh_session.recv(65535)

	remote_conn_pre.close()
	
	device = NetworkDevice(ip,username,password)
	device.parse_version_info(output)

	device.device_print()
	
	f= open("object_store.txt","wb")
	pickle.dump(device,f)
	f.close()
