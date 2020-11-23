#!/usr/bin/env python3

import subprocess
import os,sys,argparse
from termcolor import colored


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
	parser.add_argument("-v","--verbose",dest="verbose",action="store_true",help="Print filenames that are removed")
	parser.add_argument("-d","--dir",dest="directory",help="Directory to Delete Files")
	parser.add_argument("-s","--silent",dest="silent",action="store_true",help="Don't Ask confirmation")
	args = parser.parse_args()
	return args

def remove_dups():
	
	verbose = get_arguments().verbose or False

	if not get_arguments().silent:
		ans = input(colored("[Warning]","red")+colored(" Remove all Duplicate Files?(y/n): ","green"))
		if ans.lower()!="y":
			exit(0)
	
	if get_arguments().directory:
		os.chdir(get_arguments().directory)


	all_files = os.listdir()
	dic={}

	for file in all_files:		  					 #Removing Directories
		if os.path.isdir(file):
			all_files.remove(file)

	files_before_del = len(all_files)

	for file in all_files:
		try:
			output= ((subprocess.check_output(f"md5sum {file}",	shell=True)).decode()).strip()
			md5 = output.split("  ")[0]
			filename = output.split("  ")[1]

			print(colored(filename,"yellow")+"  -->  "+colored(md5+"                              ","cyan"),end="\r"),
			sys.stdout.flush()

			if md5 in dic:
				if verbose==True:
					print(colored(f"[-] Duplicate File Found --> {filename} : {md5}                              ","red"))
				os.remove(filename)
			else:
				dic[md5] = filename

		except KeyboardInterrupt:
			print("                                                                                                       ")
			is_exit = input(colored("Ctrl-c Detected. Exit?(y/n): ","red"))
			if is_exit.lower()=='y' or is_exit.lower()=='yes':
				exit()
			else:
				pass

	all_files=os.listdir()
	for file in all_files:		  					 #Removing Directories
		if os.path.isdir(file):
			all_files.remove(file)

	files_after_del = len(all_files)

	print(colored(f"[+] Total Files Before Deleting =","yellow"),colored(f"{files_before_del}                                                             ","green"))
	print(colored(f"[+] Total Files After Deleting  =","yellow"),colored(f"{files_after_del}","green"))


def main():
	banner()
	get_arguments()
	remove_dups()

main()