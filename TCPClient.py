from socket import *
serverName = 'localhost'	# 'servername'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
# print(clientSocket.getsockname())
#sentence = input('Input the name of the file you want to receive: ')
sentence = "sockets"
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()
