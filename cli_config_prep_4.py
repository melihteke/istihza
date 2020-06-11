#!/bin/python

ip_add_list = ["192.168.1.254", "192.168.2.254", "192.168.3.254","192.168.4.254","192.168.5.254","192.168.6.254"]

cli_config = """
interface GigabitEthernet %s/%s
no switchport
ip address %s 255.255.255.0
no shut
"""

x=0
y=0
z=0

for x in range(0,3):
	for y in range(0,10):
		for z in ip_add_list:
			print(cli_config %(x,y,z))

 
