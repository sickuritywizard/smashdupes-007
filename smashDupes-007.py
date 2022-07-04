#!/usr/bin/env python3

import subprocess
import os,sys,argparse
from termcolor import colored
import hashlib
from collections import defaultdict

def banner():
	toolname = """

	  _________                     .__      ________                      
	 /   _____/ _____ _____    _____|  |__   \______ \  __ ________  ______
	 \_____  \ /     \\__  \  /  ___/  |  \   |    |  \|  |  \____ \/  ___/
	 /        \  Y Y  \/ __ \_\___ \|   Y  \  |    `   \  |  /  |_> >___ \ 
	/_______  /__|_|  (____  /____  >___|  / /_______  /____/|   __/____  >
			\/      \/     \/     \/     \/          \/      |__|       \/ 
	"""

	x = "       +----------------------------------------------------------------------+"     
	y = "									🆃🆆🅸🆃🆃🅴🆁 : Killer007p\n"
	print(colored(toolname,'red'))
	print(colored(x,'blue'))
	print(colored(y,'grey'))

def get_arguments():
	parser = argparse.ArgumentParser(colored("smashdups-007.py","magenta")+"\nINFO: "+colored("Removes All Duplicate Files from the current Folder","green"))
	parser.add_argument("-v","--verbose",dest="verbose",action="store_true",help="Prints Hash of Each File")
	parser.add_argument("-d","--dir",dest="directory",help="Directory to Delete Files")
	parser.add_argument("-q","--quiet",dest="quiet",action="store_true",help="Don't Ask Confirmation")
	args = parser.parse_args()
	return args

def getHash(fileName):
	with open(fileName, "r") as f:
		fileHash = hashlib.blake2b()
		chunk = f.read(8192)
		while chunk:
			fileHash.update(chunk.encode())
			chunk = f.read(8192)
	return fileHash.hexdigest()


def printDuplicateFiles(dicts):
	print(colored(f"\n[-] DUPLICATE FILES [-]                                     \n-----------------------","cyan"))
	isEmpty = True
	for value in dicts.values():
		if len(value)>1:
			isEmpty = False
			print(value)

	if isEmpty:
		print(colored("\n[COMPLETE]","yellow" )+ colored(" No Duplicate Files Found","green"))
		exit()

def remove_dups(directory, verbose, quiet):
	if directory:
		os.chdir(directory)
	allFiles = os.listdir()
	dicts=defaultdict(list)

	for file in allFiles:		  					 #Removing Directories
		if os.path.isdir(file):
			allFiles.remove(file)

	for file in allFiles:
		try:
			hashx = getHash(file)
			if verbose==True:
				print(colored(file,"yellow")+"  -->  "+colored(hashx+"","cyan"),end="\r"),
				sys.stdout.flush()
			dicts[hashx].append(file)

		except KeyboardInterrupt:
			print("                                                                                                 ")
			is_exit = input(colored("Ctrl-c Detected. Exit?(y/n): ","red"))
			if is_exit.lower()=='y' or is_exit.lower()=='yes':
				exit()
			else:
				pass

	sys.stdout.write('\x1b[2K')
	printDuplicateFiles(dicts)
	if not quiet:
		ans = input(colored("\n[Warning]","red")+colored(" Remove all Duplicate Files?(y/n): ","green"))
		if ans.lower()!="y":
			exit(0)

	count = 0
	for duplicateList in dicts.values():
		for file in duplicateList[1:]:
			print(colored("[Deleted] ","magenta")+colored(f"{file}","blue"))
			count +=1
			try:
				os.remove(file)
			except Exception:
				print(colored("[-] Error Deleting File --> ","red")+colored(f"{file}","blue"))

	print(colored("\n[Complete]","cyan")+colored(f" Total Files Deleted = {count}","green"))


def main():
	banner()
	args = get_arguments()
	directory = args.directory or None
	quiet = args.quiet or False
	verbose = args.verbose or False
	remove_dups(directory, verbose, quiet)

main()