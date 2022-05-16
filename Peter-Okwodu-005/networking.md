
# BASIC NETWORKING

NS IP addresss for google, facebook, tesla:
- Google - 74.125.141.102
- Facebook - 31.13.67.35
- Tesla - 2.20.92.122

Breakdown of RFC ipv4 address into 4 subnets
- 10.10.10.0 (class A) (/10)
	number of hosts  = (2 ^ 24)/ required subnets
	no_of_hosts = 16,777,216/ 4 = 4,194,304
	(2 ^ n) where n = 22 host bits
	(2 ^ 22) - 2 = 4,194,302 valid hosts
	subnet mask = N . H . H . H = 11111111 . 00000000 . 00000000 . 00000000
	converted network bits = Total host bits - required host bits 
	converted network bits = 24 - 22 = 2
	new subnet mask = 11111111 . 11000000 . 11000000 . 00000000
	new subnet mask = 255 . 192 . 0 . 0
	Number of blocks required = 4,194,304/ 256 = 16,384 required blocks of address in each subnet
	first subnet = 192 . 0 . 0 . 0 to 192 . 63 . 255 . 255
	second subnet = 192 . 64 . 0 . 0 to 192 . 127 . 255 . 255
	third subnet = 192 . 128 . 0 . 0 to 192 . 191 . 255 . 255
	fourth subnet = 192 . 192 . 0 . 0 to 192 . 255 . 255 . 255
	
	
- 192.168.0.0 (class C) (/26)
	number of hosts  = (2 ^ 8)/ required subnets
	no_of_hosts = 256/ 4 = 64
	(2 ^ n) where n = 6 host bits
	(2 ^ 6) - 2 = 62 valid hosts
	subnet mask = N . N . N . H = 11111111 . 11111111 . 11111111 . 00000000
	converted network bits = Total host bits - required host bits 
	converted network bits = 8 - 6 = 2
	new subnet mask = 11111111 . 11111111 . 11111111 . 11000000
	new subnet mask = 255 . 255 . 255 . 192
	first subnet = 192 . 168 . 0 . 0 to 192 . 168 . 0 . 63
	second subnet = 192 . 168 . 0 . 64 to 192 . 168 . 0 . 127
	third subnet = 192 . 168 . 0 . 128 to 192 . 168 . 0 . 191
	fourth subnet = 192 . 168 . 0 . 192 to 192 . 168 . 0 . 255
	
- 172.168.1.0 (class B) (/18)
	number of hosts  = (2 ^ 16)/ required subnets
	no_of_hosts = 65536/ 4 = 16384
	(2 ^ n) where n = 14 host bits
	(2 ^ 14) - 2 = 16382 valid hosts
	subnet mask = N . N . H . H = 11111111 . 11111111 . 00000000 . 00000000
	converted network bits = Total host bits - required host bits 
	converted network bits = 16 - 14 = 2
	new subnet mask = 11111111 . 11111111 . 11000000 . 00000000
	new subnet mask = 255 . 255 . 192 . 0
	Number of blocks required = 16384/ 256 = 64 required blocks of address in each subnet
	(omitting the network and broadcast address)
	first subnet = 192 . 168 . 0 . 0 to 192 . 168 . 63 . 255 
	second subnet = 192 . 168 . 64 . 0 to 192 . 168 . 127 . 255
	third subnet = 192 . 168 . 128 . 0 to 192 . 168 . 191 . 255
	fourth subnet = 192 . 168 . 192 . 0 to 192 . 168 . 255 . 255
