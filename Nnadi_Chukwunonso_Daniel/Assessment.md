# (1) Session Layer 
At this layer manages sessions between machines or systems. For two device to communicate over a network a session needs to be created to ensure security(authentication and authorization). 

Authentication which verifies the identity of the machine and authorization to check the level of acesss. 

Also, in session layer checkpoints are setup during data transfer, if the session is interupted devices can resume data transfer from the last checkpoint. 


# (2) 10.10.10.0 
 * 10.10.10.1
 * 10.10.10.63
 * 10.10.10.127
 * 10.10.10.191
 * 10.10.10.255

 # 192.168.0.0
 * 192.168.0.1
 * 192.168.0.63
 * 192.168.0.91
 * 192.168.0.127
 * 192.168.0.255

# 172.168.1.0
 * 172.168.1.1
 * 172.168.1.63
 * 172.168.1.91
 * 172.168.1.127
 * 172.168.1.255


# Scrum 
SCRUM is a light weight agile process tool used by software developers that split organization into  smaller team and split work into a list of concrete deliverables. 

INDIVIDUAL INTERACTION OVER PROCESS AND TOOLS 
WORKING SOFTWARE OVER COMPREHENSIVE DOCUMENTATION 
CUSTOMER COLLABORATION OVER CONTRACT NEGOTIATION 
RESPONDING TO CHANGE OVER FOLLOWING A PLAN 


# python
from PIL import Image
basewidth = 300
picx = Image.open('Downloads\ncdc2')
widthpercent= (basewidth / float(picx.size[0]))
height = int((float(picx.size[1]) * float(widthpercent)))
picx = picx.resize((basewidth, height), Image.ANTIALIAS)
picx.save('Downloads\ncdc3')
