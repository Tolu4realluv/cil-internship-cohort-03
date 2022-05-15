NAME: SYLVIA NANEV
CANDIDATE NUMBER: 021

OSI MODEL TASK
The TCP/IP is another layered process that is similar to the OSI model. It consists of five layers namely;        

    
Application
Transport
Network
Data Link
Physical

The first four layers of the TCP/IP model (physical, data link, network, and transport layers) provide the physical standards, network interface, internetworking, and transport functions respectively that correspond to the first four layers of the OSI model. The fifth and topmost layer of the TCP/IP model (the application layer) is the combination of the application, presentation, and session layers of the OSI model. 

Application Layer: This layer is responsible for allowing users interact with applications. This layer involves protocols like the HTTP, HTTPS, SMTP, POP3, FTP, TELNET, etc and they form the basis for various services like web surfing, email, file transfer, virtual terminals, etc.

Transport Layer: This layer is responsible for the flow control, reliability, error control (with regards to data sent over the network), and segmentation of data packets (segments). It uses two protocols; Transmission Control Protocol (TCP) and User Defined Protocol (UDP). TCP is a connection-oriented transmission in that it provides feedback on the transmission of segments and ensures lost segments are retransmitted. UDP is a connectionless transmission in that it does not provide feedback on the status of the transmission and so lost segments are not retransmitted. 
Network Layer: This layer is responsible for the logical addressing (IP addressing), routing (moving data packets from source to destination), and path determination (finding the best suitable path from the source to destination) of data packets (IP datagram). This layer involves protocols like the Border Gateway Protocol (BGP), Open Shortest Path First (OSPF), Enhanced Interior Gateway Routing Protocol (EIGRP), etc. IP Addressing carried out in this layer is the process of implementing host addresses (IP addresses) used by the internet and higher layers to identify the device and to provide internetworking. These addresses belong to the networks and not the hosts using the network and only assigned (statically or dynamically)  to these devices when they connect to a network. 

Data Link Layer: This layer is responsible for physical addressing and it abstracts away the need for any other layer to care about the physical layer and what hardware is in use. The ethernet is the protocol used to send data across individual links and together with the data link layer, they provide a means for higher levels of the stack to send and receive data. The physical addressing carried out in this layer is the assigning of the Media Access (MAC) address to the individual network interfaces attached to the network devices. This MAC address is a 48-bit number normally represented by six groupings of two hexadecimal numbers. 

Physical Layer: This layer is responsible for cabling connectors and converting the binary bits to signals through the local media (copper wire (electrical signals)), (optical fibre (light signals)), and (wireless using the air (radio waves signals)).

BASIC NETWORKING TASK
The NS IP address for Google, Facebook and Tesla are:
Google: 2c0f:fb50:4003:802::200e
              216.58.223.238

Facebook: 2a03:2880:f11f:83:face:b00c:0:25de
                  179.60.192.36


Tesla: 23.201.26.71
          104.86.104.55
          184.30.18.203
          2.20.92.122
          104.89.119.127
          184.50.204.169

b. Breakdown 10.10.10.0, 192.168.0.0, and 172.168.1.0 to four subnets with no address leftover. 

10.10.10.0
•	This is a class A network, with a default CIDR of /8.
In order to get 4 subnets, we need to borrow 2 bits from the second octet so that, 
•	Number of Subnets = 2^2 = 4
Since we borrowed two bits and converted them from 0 to 1, the remainder of host bits equal to 0 is equal to 24-2 = 22.
•	Number of hosts in a subnet = (2^22) – 2 = 4,194,302
Therefore, out of the two (2) borrowed host bits, the first is equal to 2^7 = 128 and the second is equal to 2^6 = 64. The sum of all of this is equal to 128+64 = 192.
•	Block size: 256-192 = 64.
	Network Address	Broadcast Address
1st Subnet	10.0.0.0	10.63.255.255
2nd Subnet	10.64.0.0	10.127.255.255
3rd Subnet	10.128.0.0	10.191.255.255
4th Subnet	10.192.0.0	10.255.255.255

	Range of Host Addresses
1st Subnet	10.0.0.1 - 10.63.255.254
2nd Subnet	10.64.0.1 - 10.127.255.254
3rd Subnet	10.128.0.1 - 10.191.255.254
4th Subnet 	10.192.0.1 - 10.255.255.254

192.168.0.0
•	This is a class C network, with a default CIDR of /24.
In order to get 4 subnets, we need to borrow 2 bits from the fourth octet so that, 
•	Number of Subnets = 2^2 = 4
Since we borrowed two bits and converted them from 0 to 1, the remainder of host bits equal to 0 is equal to 8-2 = 6.
•	Number of hosts in a subnet = (2^6) – 2 = 62
Therefore, out of the two (2) borrowed host bits, the first is equal to 2^7 = 128 and the second is equal to 2^6 = 64. The sum of all of this is equal to 128+64 = 192.
•	Block size: 256-192 = 64.
	Network Address	Broadcast Address
1st Subnet	192.168.0.0	192.168.0.63
2nd Subnet	192.168.0.64                                                                                      	192.168.0.127
3rd Subnet	192.168.0.128	192.168.0.191
4th Subnet	192.168.0.192	192.168.0.255

	Range of Host Addresses
1st Subnet	192.168.0.1 - 192.168.0.62
2nd Subnet	192.168.0.65 - 192.168.0.126
3rd Subnet	192.168.0.129 - 192.168.0.190
4th Subnet 	192.168.0.193 - 192.168.0.254


172.168.1.0
•	This is a class B network, with a default CIDR of /16.
In order to get 4 subnets, we need to borrow 2 bits from the third octet so that, 
•	Number of Subnets = 2^2 = 4
Since we borrowed two bits and converted them from 0 to 1, the remainder of host bits equal to 0 is equal to 16-2 = 14.
•	Number of hosts in a subnet = (2^14) – 2 = 16,382
Therefore, out of the two (2) borrowed host bits, the first is equal to 2^7 = 128 and the second is equal to 2^6 = 64. The sum of all of this is equal to 128+64 = 192.
•	Block size: 256-192 = 64.
	Network Address	Broadcast Address
1st Subnet	172.168.0.0	172.168.63.255
2nd Subnet	172.168.64.0                                                                                      	172.168.127.255
3rd Subnet	172.168.128.0	172.168.191.255
4th Subnet	172.168.192.0	172.168.255.255

	Range of Host Addresses
1st Subnet	172.168.0.1 - 172.168.63.254
2nd Subnet	172.168.64.1 - 172.168.127.254
3rd Subnet	172.168.128.1 - 172.168.191.254
4th Subnet 	172.168.192.1 – 172.168.255.254


SOFTWARE DEVELOPMENT PROCESS TASKS
1.	Scrum is a software product development strategy that organizes software developers as a team to reach a common goal thereby creating a ready for market product. It focuses on splitting your organization into small, cross-functional, self-organizing teams, and splitting your work into a list of small, concrete deliverables, and sorting the list by priority and estimating the relative effort of each item. Scrum also focuses on splitting your time into short fixed-length iterations/sprints (usually 2-4 weeks), with potentially shippable code demonstrated after each iteration. 
Scrum Benefits n Software Development
•	The incremental process shortens the time to market by about 30 percent to 40 percent, because the product owner is part of the scrum team, requirements can be delivered as they are needed. 
•	Scrum projects often realize a higher return on investment (ROI) due to conditions like; decreased time to market, defects that are fewer and less costly, projects failing early and quickly when it’s less costly.
•	Project focus and goals can change with evolving business goals.
•	Each sprint produces a product that is ready for market even though the project is ongoing. 
•	Reviewing each sprint before the team moves on to the next sprint spreads testing throughout development. 
2.	From the Agile Manifesto:
Working with software over comprehensive documentation
Customer collaboration over contract negotiation
Responding to change over following a plan







