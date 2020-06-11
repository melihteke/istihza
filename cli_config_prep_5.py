#!/bin/python

port_list = ["0/1", "0/2", "0/3", "0/4", "0/5", "0/6"]
ip_add_list = ["192.168.1.254", "192.168.2.254", "192.168.3.254","192.168.4.254","192.168.5.254","192.168.6.254"]

cli_config = """
interface GigabitEthernet %s
no switchport
ip address %s 255.255.255.0
no shut
"""

x=0
y=0
for x in port_list:
	print(cli_config %(x, ip_add_list[y]))
	y=y+1
 
