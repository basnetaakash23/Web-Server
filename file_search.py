import os
from os.path import join



def search_for_file(filename):
	query = filename
	#print(query)
	for root, dirs, files in os.walk('/Users/aakashbasnet/Desktop/'):
		for file in files:
			if(query == file):
				print(file)
				print(os.path.abspath(os.path.join(root, file)))
				f = open(os.path.abspath(os.path.join(root, file)),'rb')
				l = f.read(1024)
				while (l):
					print(l)
					l = f.read(1024)
					print('\n')

				f.close()
				

directory_search = raw_input("Input the name of the file you want to receive:")
print(directory_search)
search_for_file(directory_search)


