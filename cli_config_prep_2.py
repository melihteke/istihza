#!/bin/python3
cisco_config="""
interface GigabitEthernet %s/%s
switchport mode access
switchport access vlan %s
switchport port-security
switchport port-security maximum 5
switchport port-security mac-address sticky
"""

vlan=input("Please specify the access port vlans: ")
i=0
x=0
for i in range(0,5):
	y=1
	for y in range(0,48):
		print(cisco_config % (i,y,vlan))
print("Config generation is completed")
