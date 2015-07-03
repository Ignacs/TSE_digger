# -** coding: utf-8 -*-
import os
import traceback

print ('\n\n')

def start():
	address = "/home/ignacs"
	try:
		Folders = []
		Id = 1
		for item in os.listdir(address):
			endaddress = address + "/" + item
			Folders.append({'Id': Id, 'TopId': 0, 'Name': item, 'Address': endaddress })
			Id += 1         

			state = 0
			for item2 in os.listdir(endaddress):
				state = 1
				
			if state == 1: 
				Id = FolderToList(endaddress, Id, Id - 1, Folders)
		return Folders
	except:
		print ("___________________________ ERROR ___________________________\n" + traceback.format_exc())

def FolderToList(address, Id, TopId, Folders):
	for item in os.listdir(address):
		endaddress = address + "/" + item
		Folders.append({'Id': Id, 'TopId': TopId, 'Name': item, 'Address': endaddress })
		Id += 1

		state = 0
		for item in os.listdir(endaddress):
			state = 1
		if state == 1: 
			Id = FolderToList(endaddress, Id, Id - 1, Folders)
	return Id

print (start())
