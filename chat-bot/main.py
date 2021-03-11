import sys
sys.path.append(sys.path[0]+"\\lib")
from responsechatbot import ChatbotResponse as cr

reply = cr.getResponse("how far is kelowna from vancouver?")
print(reply)