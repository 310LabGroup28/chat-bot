import socket
from responsechatbot import ChatbotResponse as cr

IP = 'PLACEHOLDER_IP'
PORT = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(5)
clientsocket, address = s.accept()

msgSend = "Hi Vin, big fan!\n"
for i in range(15):

	clientsocket.send(bytes(msgSend, "utf-8"))
	print("Chatbot: " + msgSend)

	msgRec = clientsocket.recv(1024)
	msgRec = msgRec.decode("utf-8")
	print("Vinbot: " + msgRec+"\n")

	msgSend = cr.getResponse(msgRec)