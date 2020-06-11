
#!/bin/python

config_data =  {"192.168.1.1" : {"hostname":"Router1",
								"secret_pass" : "cisco",
								"snmp_comm":"snmp_cisco"},
				"192.168.2.1" : {"hostname":"Router2",
								"secret_pass" : "nokia",
								"snmp_comm":"snmp_nokia"},
				"192.168.3.1" : {"hostname":"Router3",
								"secret_pass" : "juniper",
								"snmp_comm":"snmp_juniper"},
				"192.168.4.1" : {"hostname":"Router4",
								"secret_pass" : "arista",
								"snmp_comm":"snmp_arista"},
				"192.168.5.1" : {"hostname":"Router5",
								"secret_pass" : "cumulus",
								"snmp_comm":"snmp_cumulus"}}

device = input("Please select your device: ")


print("conf ter\n")
print("hostname %s" %(config_data[device]["hostname"]))
print("enable secret %s" %(config_data[device]["secret_pass"]))
print("snmp community %s rw" %(config_data[device]["snmp_comm"]))





