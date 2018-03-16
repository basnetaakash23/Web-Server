from socket import *
serverName = 'localhost'	# 'servername'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
# print(clientSocket.getsockname())
directory_search = input('Input the name of the file you want to receive: ')
#sentence = "sockets"
clientSocket.send(directory_search.encode())
reply = clientSocket.recv(1024)
print('From Server: ', reply.decode())
clientSocket.close()
