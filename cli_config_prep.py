#!/bin/python3
cisco_config="""
interface GigabitEthernet %s/%s
switchport mode access
switchport access vlan %s
switchport port-security
switchport port-security maximum 5
switchport port-security mac-address sticky
"""

print(cisco_config % ("1","1","100"))
