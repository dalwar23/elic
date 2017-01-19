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
import ftplib
import datetime

# Define a function to download required file/s
def download(flag):
	# Introduce login credentials as global variables
	global ftpHost
	global ftpUsername
	global	ftpPassword
	# Assign variables
	ftpHost = 'ftp.pysource.org'
	ftpUsername = 'elic@pysource.org'
	ftpPassword = 'shAd0wf@x1102'
	# Create a ftp connection and login
	print('Trying to login to [ {} ]'.format(ftpHost), end='\n')
	try:
		ftp = ftplib.FTP(ftpHost,ftpUsername,ftpPassword)
		print('Logged in.', end='\n')
	except:
		print('FTP login Error!', end='\n')
	# Determine file type and Directory
	if flag == 'dFiles':
		# Change working directory to '/downloads/dependencies'
		cWD = ftp.cwd('/downloads/dependencies')
		downloadList = getDownloadList(flag)
	elif flag == 'mFiles':
		# Change working directory to '/downloads/messages'
		cWD = ftp.cwd('/downloads/messages')
		downloadList = getDownloadList(flag)
	elif flag == 'kFiles':
		# Change working directory to '/downloads/keys'
		cWD = ftp.cwd('/downloads/keys')
		downloadList = getDownloadList(flag)
	# Now download necessary file/s
	if flag == 'mFiles':
		# Show list and download selected file
	else:
		# download all files
# Define a function to get downloadable file list
def getDownloadList(flag):
	# Create a list of download files
	downloadList = []
	try:
		fileList = ftp.nlst()
		if not fileList:
			print('No files detected in [ {} ] directory'.format(cWD), end='\n')
		else:
			for item in fileList:
				if flag == 'dFiles' and item.endswith('.exe') or item.endswith('.dll'):
					downloadList.append(item)
				elif flag == 'mFiles' or flag == 'kFiles' and item.endswith('.asc')
					downloadList.append(item)
	except:
		print('Can not list files in directory [ {} ]'.format(cWD), end='\n')
	return downloadList
# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
  main()