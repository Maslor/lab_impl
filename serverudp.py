# udp-server.py

# TFTP Opcodes

import socket
hostPort = 5005
modeserver = ""
firstUsername = ""
firstDestUser = ""
secondusername = ""
secondDestUser = ""

ServerMsg = "Nice to meet you!"	
ServerSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)	
ServerSock.bind	((hostIP,hostPort))	
(ClientMsg,(ClientIP,ClientPort))= ServerSock.recvfrom(1024)
ServerSock.sendto(ServerMsg,(ClientIP, ClientPort))
ServerSock.close()

def register(originName,destName,mode):
	#verificação do user
	if firstusername == "":
		firstusername = originName
		firstDestUser = destName
		
	else:
		secondusername = originName
		secondDestUser = destName

	#verificação do modo
	if mode == modeserver:
		#errormessage
	else:
		modeserver=mode




	 

