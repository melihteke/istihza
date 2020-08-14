#!/bin/python3

from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.178.64',
    'username': 'admin',
    'password': 'cisco'
}

net_connect = ConnectHandler(**iosv_l2)
print(net_connect.find_prompt())                  #shows actual prompt
output = net_connect.send_command('show ip int brief')      #sends only single cli command
print (output)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0'] #sends sets of commands
output = net_connect.send_config_set(config_commands)
print (output)

#for n in range (100,105,1):
#    print ("Deleting  VLAN " + str(n))
#    config_commands = ['no vlan ' + str(n)]
#    output = net_connect.send_config_set(config_commands)
#    print (output)
config_commands = ['no vlan ' + '2-1000']
output = net_connect.send_config_set(config_commands)
print (output)
