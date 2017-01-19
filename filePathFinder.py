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

# Define a function to find script directory path
def findScriptDir():
	scriptPath = os.path.realpath(__file__)
	# Directory of this script and dependency files' directory
	scriptDir = os.path.dirname(scriptPath)
	return scriptDir
# Define a function to find dependency files directory
def findDepFilesDir():
	pathSep = '/'
	scriptDir = findScriptDir()
	depFilesDir = scriptDir + pathSep + 'gpg' + pathSep
	return depFilesDir
# Define a function to find key files directory
def findKeyFilesDir():
	pathSep = '/'
	scriptDir = findScriptDir()
	keyFilesDir = scriptDir+pathSep+'keys'+pathSep
	return keyFilesDir
# Define a function to find message file directory
def findMsgFilesDir():
	pathSep = '/'
	scriptDir = findScriptDir()
	msgFilesDir = scriptDir+pathSep+'messages'+pathSep
	return msgFilesDir
# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
  main()