import getpass
import telnetlib

HOST = "192.168.178.54"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii') + b"\n")
	tn.write(b"enable\n")
	tn.write(b"cisco\n")
	tn.write(b"conf t\n")
	tn.write(b"int loop 20\n")
	tn.write(b"ip address 20.1.1.1 255.255.255.255\n")
	tn.write(b"int loop 21\n")
	tn.write(b"ip address 21.2.2.2 255.255.255.255\n")
	tn.write(b"router ospf 4\n")
	tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
	tn.write(b"end\n")
	tn.write(b"exit\n")
	print(tn.read_all().decode('ascii'))

	with open("telnet_config.txt", "w") as f:
		print("telnet_config.txt file is created")
		f.write("enable\n")
		f.write("conf t\n")
		f.write("int loop 20\n")
		f.write("ip address 20.1.1.1 255.255.255.255\n")
		f.close()
