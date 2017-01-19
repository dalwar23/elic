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

# Import custom libraries
import filePathFinder
import fileDownloader
import dependencyChecker
import networkConnectionChecker
import fileDecrypter

# Create main function to process threads
def main():
	# Check Internet connection is available or not
	netStat = networkConnectionChecker.is_connected()
	if netStat == True:
		print('INTERNET connection detected.', end='\n')
		# Required files to run this program, dependency file list
		dependecyList = ['gpg.exe','iconv.dll']
		# Directory path of this very script
		scriptDir = filePathFinder.findScriptDir()
		# Find dependency files directory
		depFilesDir = filePathFinder.findDepFilesDir()
		# Check for dependent files
		dependencyCheckResult = dependencyChecker.check(dependecyList,depFilesDir)
		# Check for dependencyChecker's result
		if dependencyCheckResult == True:
			pass
		elif dependencyCheckResult == False:
			print('Initiating download......', end='\n')
			print('------------ ***** ------------', end='\n')
			flag = 'dFiles'
			downloadResult = fileDownloader.download(depFilesDir,flag)
			if downloadResult == True:
				pass
			else:
				print('Program is unable to download required files.', end='\n')
		# Download and decrypt files
		# Download file
		downloadFile = ftpFileDownloader.download()
		# Decrypt file
		decryptFile = fileDecrypter.decrypt()
	else:
		print('Oooppppsss! No INTERNET connection detected.','Please check your network connection!!', sep='\n',end='')

# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
  main()