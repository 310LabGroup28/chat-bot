import socket
from responsechatbot import ChatbotResponse as cr

IP = 'PLACEHOLDER_IP'
PORT = 4000

# Open a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind socket to local IP
s.bind((IP, PORT))
s.listen(5)
# Accept connection from client
clientsocket, address = s.accept()

# Starting message since both bots expect the user to send the first input
msgSend = "Hi Vin, big fan!\n"
# Stop after 15 turns each
for i in range(15):
	# Send current message
	clientsocket.send(bytes(msgSend, "utf-8"))
	print("Chatbot: " + msgSend)

	# Receive a response
	msgRec = clientsocket.recv(1024)
	msgRec = msgRec.decode("utf-8")
	print("Vinbot: " + msgRec+"\n")

	# Get the next thing to send
	msgSend = cr.getResponse(msgRec)