import os
from os.path import join



def search_for_file(filename):
	query = filename
	#print(query)
	for root, dirs, files in os.walk('/Users/aakashbasnet/Desktop/'):
		for dir in dirs:
			if(query in dir):
				print(query)
				print(dir)
				print('\n')


search_for_file('sockets')


