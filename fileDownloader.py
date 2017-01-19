#!/usr/bin/python -tt
# ***************************************************
# This program encrypts/decrypts data file/s.		*
# Author: Md Dalwar Hossain Arif					*
# E-mail: dalwar0143@gmail.com						*
# Last Update: 18-03-2015 01:22 AM					*
# Copyright: Md Dalwar Hossain Arif					*
# ***************************************************

# Import default libraries
from __future__ import ( division, absolute_import, print_function, unicode_literals )
import sys, os, tempfile, logging

# Check version and import correct libraries
if sys.version_info >= (3,):
	import urllib.request as urllib2
	import urllib.parse as urlparse
else:
	import urllib2
	import urlparse
	
# Define a function to execute the download
def downloadFile(dstDir, url, desc=None):
	# Try to open a specific URL and get all meta information
	try:
		u = urllib2.urlopen(url)
	except URLError as e:
		if hasattr(e, 'reason'):
			print('Program has failed to reach the server.', end='\n')
			print('Most probable reason: {}'.format(e.reason), end='\n')
		elif hasattr(e, 'code'):
			print('Server was unable to fulfill the request.', end='\n')
			print('Error Code: {}'.format(e.code))
		else:
			pass
	finally:
		pass
	# Get file name extracted
	scheme, netloc, path, query, fragment = urlparse.urlsplit(url)
	filename = os.path.basename(path)
	if not filename:
		filename = 'downloaded.file'
	if desc:
		filename = os.path.join(desc, filename)
	# Get header information and initiate download
	filePath = dstDir + filename
	with open(filePath, 'wb') as f:
		meta = u.info()
		file_size = int(meta['Content-Length'])
		print("File Name -> [ {} ]\nDownload Path -> [ {} ]\nFile Size (in bytes) -> [ {} ]".format(filename, url, file_size))

		file_size_dl = 0
		block_sz = 8192
		while True:
			buffer = u.read(block_sz)
			if not buffer:
				break
			# Write files
			file_size_dl += len(buffer)
			f.write(buffer)
		# Print status message
		status = "{0:16}".format(file_size_dl)
		if file_size:
			status += "   [{0:6.2f}%]".format(file_size_dl * 100 / file_size)
		status += chr(13)
		print(status, end="")
	print()

	return filename
# Define download() function to initiate download
def download(dstDir,flag):
	# Choose right list of files to download
	if flag == 'dFiles':
		urlList = ['http://www.elic.pysource.org/downloads/dependencies/gpg.exe',
				'http://www.elic.pysource.org/downloads/dependencies/iconv.dll']
	elif flag == 'mFiles':
		urlList=[]
	elif flag == 'kFiles':
		urlList=[]
	# Download file according to list
	fileCount = 0
	for url in urlList:
		filename = downloadFile(dstDir,url)
		print('[ {} ] Download Complete.'.format(filename), end='\n')
		print('------------ ***** ------------', end='\n')
		if filename:
			fileCount += 1
		else:
			pass
	if fileCount == len(urlList):
		return True
	else:
		return False
# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()
