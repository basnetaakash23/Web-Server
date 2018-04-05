import os
from os.path import join
from socket import *

def search_for_file(filename):
	
	query = filename
	#print(query)
	for root, dirs, files in os.walk('/Users/aakashbasnet/Desktop/'):
		for file_ in files:
			if file_ == filename:
				#print(query)
				#print(dirs)
				#print('\n')
				file_path = os.path.abspath(os.path.join(root, file_))

	return file_path


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
	path_of_file = search_for_file(file_name)
	f = open(path_of_file,'rb')
	l = f.read(1024)
	while (l):
		connectionSocket.send(l)
		l = f.read(1024)

	f.close()
	connectionSocket.send("Connection has ended")
	connectionSocket.close()

	#capitalizedSentence = sentence.upper()
	# reply = "File not Found!"
	# for root, dirs, files in os.walk('/Users/aakashbasnet/Desktop/'):
	# 	for dir_ in dirs:
	# 		print(dir_)
	# 		print('\n')
	# 		if(file_name in dir_):
	# 			reply = "File you requested has been found!"

	#reply = search_for_file(file_name)
	



