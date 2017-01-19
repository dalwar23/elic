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

# Define a function dependencyChecker(dependecyList,depFilesDir) to check for required files
def check(dependecyList,depFilesDir):
	# Check dependecyList against all files in the dependency files directory
	count = 0
	# List all files in 'script' directory
	fileNames = next(os.walk(depFilesDir))[2]
	# Check against dependecyList and count
	for item in dependecyList:
		if item in fileNames:
			count += 1
	# Checking whether all required files are present or not
	if count == len(dependecyList):
		print('All the required files are present.', end='\n')
		return True
	else:
		print('All the required files are not present.', end='\n')
		return False	
# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()
