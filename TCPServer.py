import os
from os.path import join
from socket import *

def search_for_file(filename):
	query = filename
	#print(query)
	for root, dirs, files in os.walk('/Users/aakashbasnet/Desktop/'):
		for dir_ in dirs:
			if(query in dir_):
				#print(query)
				#print(dirs)
				#print('\n')
				return "File has been found"

	return "File not found"


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while 1:
	connectionSocket, addr = serverSocket.accept()
	print(connectionSocket.getpeername())
	file_name = connectionSocket.recv(1024)
	
	file_name = file_name.decode()
	print("The file name is", file_name)
	reply = search_for_file(file_name)
	#capitalizedSentence = sentence.upper()
	# reply = "File not Found!"
	# for root, dirs, files in os.walk('/Users/aakashbasnet/Desktop/'):
	# 	for dir_ in dirs:
	# 		print(dir_)
	# 		print('\n')
	# 		if(file_name in dir_):
	# 			reply = "File you requested has been found!"

	#reply = search_for_file(file_name)
	connectionSocket.send(reply.encode())
	connectionSocket.close()



