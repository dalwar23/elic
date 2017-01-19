#!/usr/bin/python -tt
# ***************************************************
# This program encrypts/decrypts data file/s.		*
# Author: Md Dalwar Hossain Arif					*
# E-mail: admin@pySource.org;dharif23@gmail.com		*
# Website: www.pySource.org							*
# Date:	18-Mar-2015									*
# Time:	01:20 AM									*
# Last Update: 18-03-2015 01:21 AM					*
# Copyright: Md Dalwar Hossain Arif					*
# License: GPL										*
# ***************************************************

# Import default libraries
import socket

# Try to connect to world's most common site
REMOTE_SERVER = "www.google.com"

# Create a function to check network connection
def is_connected():
  try:
    # see if we can resolve the host name -- tells us if there is a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually reachable
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False
# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()