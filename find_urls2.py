#!/usr/bin/python
import requests
import urllib
import time
import os
import argparse
import re
from colorama import Style,Fore
from multiprocessing import Pool

def arguments():

	print Style.BRIGHT + Fore.CYAN + """

 __   __  ______    ___      _______ 
|  | |  ||    _ |  |   |    |       |
|  | |  ||   | ||  |   |    |  _____|
|  |_|  ||   |_||_ |   |    | |_____ 
|       ||    __  ||   |___ |_____  |
|       ||   |  | ||       | _____| |
|_______||___|  |_||_______||_______|

	(SSRF HELPER)

	"""+Fore.WHITE+"""@z0idex"""

	global args
	parser = argparse.ArgumentParser(description="Searches for URLS in a list")
	parser.add_argument("-d", "--domain", help="The domain", required=True)
	parser.add_argument("-s", "--source", help="Source file (urls or js)", required=True)
	parser.add_argument("-t", "--threads", help="number of threads", required=True)
	parser.add_argument("-o", "--output", help="output urls to a file", required=True)
	args = parser.parse_args()

	if args.source != None:
		if os.path.isfile(args.source):
			global save
			save = open(args.output, 'w+')
			print Style.BRIGHT + Fore.WHITE + "\n[" + Fore.BLUE + "+" + Fore.WHITE + "] Searching for External sources"
			pool = Pool(int(args.threads))			
			with open(args.source) as file:
				results = pool.map(find_urls, file, int(args.threads))
			save.close()


def cnt_substr(inp_str, sub_str):
	inp_join_str = ''.join(inp_str.split())
	sub_join_str = ''.join(sub_str.split())
	return inp_join_str.count(sub_join_str)


def find_urls(url):

	url = url.split()[0]
	Count = cnt_substr(url, args.domain)
	if Count == 1:
		link = urllib.unquote(url)
		b = re.search("=https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", link)
		if b != None:
			try:
				r = requests.get(link, verify=True)
				print Style.BRIGHT + Fore.WHITE + "\n[" + Fore.GREEN + "+" + Fore.WHITE + "] " + Fore.GREEN + "FOUND: " + Fore.WHITE + "[ " + Fore.BLUE + str(r.status_code) + Fore.WHITE + " ] "  + Fore.WHITE+ link
				save.write(link + "\n")	
			except:
				pass

arguments()
