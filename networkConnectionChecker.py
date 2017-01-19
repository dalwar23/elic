#!/usr/bin/python -tt
# ***************************************************
# This program encrypts/decrypts data file/s.       *
# Author: Md Dalwar Hossain Arif                    *
# E-mail: dalwar0143@gmail.com                      *
# Last Update: 18-03-2015 01:22 AM                  *
# Copyright: Md Dalwar Hossain Arif                 *
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