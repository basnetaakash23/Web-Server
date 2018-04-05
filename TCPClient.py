from socket import *
serverName = 'localhost'	# 'servername'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
# print(clientSocket.getsockname())
directory_search = raw_input('Input the name of the file you want to receive: ')
#sentence = "sockets"
clientSocket.send(directory_search.encode())
with open('received_file','wb') as f:
	print('file opened')
	while True:
		data = clientSocket.recv(1024)
		if not data:
			break

		f.write(data)
 

clientSocket.close()
