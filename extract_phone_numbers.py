'''
@author: Neha Pawar
@date: 29.12.2016

Program to extract all the telephone numbers(base 10 -digit format indian mobile numbers and its variation)
from a directory which contains only text files
'''

import re
import os 
from os.path import exists


root_dir=raw_input("Enter the directory path: ")

for curr_dir,sub_dirs,files in os.walk(root_dir):
	print "Current directory is:",curr_dir
	for file_item in files:
		fname = os.path.join(curr_dir,file_item)
		if os.path.exists(fname):
			with open(fname) as f:
				for line in f:
					result=re.findall('(?:0|\+91-?)?[7-9]\d{9}',line)
					print result
		else:
			print "File does not exist"

