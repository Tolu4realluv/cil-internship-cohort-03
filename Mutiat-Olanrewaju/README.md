# 1. Description of a layered model similar to OSI

The layered model similar to OSI is TCP because they are both network reference models and divide network communication process into layers. <br>
The Transmission Control Protocol (TCP) is a transport protocol that is used on top of IP to ensure reliable transmission of packets. The fact that it is used on top of IP, it is sometimes refered to as TCP/IP. <br>
TCP includes mechanisms to solve many of the problems that arise from packet-based messaging, such as lost packets, out of order packets, duplicate packets, and corrupted packets. <br>
TCP/IP is a five(5) model layers which include; Application, Transport, Internet or Network, Data Link, and Physical layer. <br>

- Application layer: This layer defines the protocols and standards that an application requires to connect to the network. For example, an application layer protocol HTTP defines how a web browser can fetch a web page from a web server.
- Transport layer: This layer can also be called host-to-host layer. It provides a logical connection between two hosts. It functionalities are segmentation, reliability, flow control and connection multiplexing.
- Internet and Network layer: In the original TCP/IP model, this layer is defined as the Internet layer. In the updated version, it is renamed to the Network layer. The main functions of this layer are addressing and routing. For these functions, it uses IP protocol.
- Link layer (Data link and Physical layer): his layer defines standards and protocols for data transmission and physical connectivity. It also provides hardware addressing that is used to locate a device in the local network. Switching and connecting devices are the two main functions of this layer.

# 2. Basic Networking

- NS IP Address for Google : 216.58.223.206
- NS IP Address for Facebook: 102.132.101.35
- NS IP Adresses for Tesla: 23.201.26.71, 184.30.18.203, 184.50.204.169, 2.20.92.122, 104.89.119.127, 104.86.104.55 <br><br>
  Breakdown the following RFC 1918 IPv4 address range into exactly 4 subnets with no address left over.
  * **10.10.10.0/10** : 10.10.10.0, 10.10.10.64, 10.10.10.128, 10.10.10.192
  * **192.168.0.0/26** : 192.168.0.0, 192.168.64.0, 192.168.128.0, 192.168.192.0
  * **172.168.1.0/18** : 172.164.1.0, 172.164.1.64, 172.164.1.128, 172.164.1.192

# 3. Software Development Process

### **Scrum** is the leading agile development method for completing projects with a complex, innovative scope of work. <br>
Scrum framework:

- A product owner creates a prioritized wish list called a product backlog.
- During sprint planning, the team pulls a small chunk from the top of that wish list, a sprint backlog, and decides how to implement those pieces.
- The team has a certain amount of time, a sprint, to complete its work usually two to four weeks but meets each day to assess its progress (daily Scrum).
- Along the way, the ScrumMaster keeps the team focused on its goal.
- At the end of the sprint, the work should be potentially shippable, as in
  ready to hand to a customer, put on a store shelf, or show to a
  stakeholder.
- The sprint ends with a sprint review and retrospective.
- As the next sprint begins, the team chooses another chunk of the product backlog and begins working again.

Benefit of Scrum in software development

- **Periodic delivery for continous improvement**: It is important to make periodic deliveries to have the possibility of adding functionalities to the product in an incremental way. Periodic deliveries provide space for continuous improvement while allowing us to manage customer expectations better and to adapt to his/her need.
- **Autonomy and empowerment**: One of the great benefits of Scrum is the high degree of autonomy the team members acquire, encouraging and empowering them to perform increasingly complex tasks, thus distributing knowledge knowing that, if necessary, there is another member who is able to perform a certain task.
-**Product quality to have happy clients**: Metrics are used to get the product to have high quality standards with partial deliveries every 2 weeks. The metrics are calculated each time an iteration ends and determines how the progress is in the development of the product allowing the team to concentrate on those things to improve in order to deliver the best restult.

## From the Agile Manifesto, complete the following:
- Individuals and interactions over **processess and tools**
- Working software over **comprehensive documentation**
- Customer collaboration over **contract negotiation**
- Responding to change over **following a plan**


