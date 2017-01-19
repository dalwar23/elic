#!/usr/bin/python -tt
# ***************************************************
# This program encrypts/decrypts data file/s.		*
# Author: Md Dalwar Hossain Arif					*
# E-mail: dalwar0143@gmail.com						*
# Last Update: 18-03-2015 01:22 AM					*
# Copyright: Md Dalwar Hossain Arif					*
# ***************************************************

# Import default libraries
import os
import sys
import gnupg
import getpass

# Import custom libraries
import filePathFinder

# Define a function to decrypt files
def decrypt():
	# Get dependency file directory and script file directory
	# Directory path of this script
	scriptDir = filePathFinder.findScriptDir()
	# Directory path of dependency files
	depFilesDir = filePathFinder.findDepFilesDir()
	# Directory path of key files 
	keyFilesDir = filePathFinder.findKeyFilesDir()
	# Directory path of message file
	msgFilesDir = filePathFinder.findMsgFilesDir()
	# Load private key file into program
	print('Program will now load private key file.', end='\n')
	try:
		gpg = gnupg.GPG(gnupghome=depFilesDir)
		gpg.encoding = 'utf-8'
	except:
		print('Can not locate GNUPG.', end='\n')
	try:
		pvtKeyFileName = 'private.asc'
		pvtKeyPath = keyFilesDir + pvtKeyFileName
		key_data = open(pvtKeyPath).read()
	except:
		print('Unable to read private key file.', end='\n')
	try:
		importResult = gpg.import_keys(key_data)
		keyFingerPrint = importResult.fingerprints
		print('Private key with fingerprint [ {} ] is loaded.'.format(keyFingerPrint[0]), end='\n')
	except:
		print('Can not import private key file.', end='\n')

	# Scan for 'PASSPHRASE' from the user to decrypt file
	password = getpass.getpass(prompt='Please enter your private key passphrase : ')

	# Now it's time to decrypt file/s
	encryptedFileName = 'Test.txt.asc'
	decryptedFileName = 'Test_d.txt'
	with open(msgFilesDir+encryptedFileName,'rb') as eFile:
		status = gpg.decrypt_file(eFile, passphrase=password, output=msgFilesDir+decryptedFileName)
	if status.ok == True:
		print('File Decryption Successful.', end='')
		return True
	else:
		print('File could not be decrypted.','Most common reason: PASSPHRASE is wrong! Please check and try again!', end='', sep='\n')
		return False
# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
  main()