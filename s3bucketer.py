#!/usr/bin/python

# Import modules
import time
import sys
import os
import requests
import argparse

# Import more modules
from colorama import Fore,Style


def banner():
	os.system("clear")
        print Style.BRIGHT + Fore.WHITE + """

     ______________              _                          
    (_______(____  \            | |         _               
  ___  ____  ____)  )_   _  ____| |  _ ____| |_  ____  ____ 
 /___)(___ \|  __  (| | | |/ ___) | / ) _  )  _)/ _  )/ ___)
|___ |____) ) |__)  ) |_| ( (___| |< ( (/ /| |_( (/ /| |    
(___(______/|______/ \____|\____)_| \_)____)\___)____)_|    
                                                            
             """ + Style.DIM + Fore.BLUE + "\t\t@z0idex\n\n"



class Scanner(object):
    """docstring for Scanner"""
    def __init__(self, args):
        super(Scanner, self).__init__()
        self.args = args
        

    # Print the text
    def text(self,status, text):
        if status == "i":
                print Style.BRIGHT + Fore.WHITE + "["+Fore.YELLOW+"i"+Fore.WHITE+"]" + " " + Style.RESET_ALL + Style.DIM + Fore.WHITE + text

        if status == "!":
                print Style.BRIGHT + Fore.WHITE + "["+Fore.RED+"!"+Fore.WHITE+"]" + " " + Style.RESET_ALL + Style.DIM + Fore.WHITE + text

        if status == "+":
                print Style.BRIGHT + Fore.WHITE + "["+Fore.GREEN+"+"+Fore.WHITE+"]" + " " + Style.RESET_ALL + Style.DIM + Fore.WHITE + text


    # Bucket checker
    def checker(self,domain):

        if os.path.isfile(self.args.buckets) == None:
                self.text("!", "No bucket wordlist")
                return

        buckets = open(self.args.buckets, "r")
        for bucket in buckets.readlines():
                # Strip the bucket
                bucket = bucket.strip() 
	        # Check the prefix / seperator
        	for i in range(3):
                	        
			seperator = ""
                        		
			if i == 0:
                        	seperator = "_"
                       	if i == 1:
                               	seperator = "-"
                       	if i == 2:
                               	seperator = "."
			
			for i in range(2):
				if i == 0:

					url = ("https://%s%s%s.s3.amazonaws.com" % (bucket, seperator, domain))
					if args.quite == "0":
						self.text("i", url)
                        		# Try to get the response a check the status_code for a bucket
                  			try:
                        			# make a request
 		                		response = requests.get(url, verify=True, timeout=10)
                	        		# Access Denied
                        			if response.status_code == 403:
                	              			self.text("!", "Found Bucket: %s (%s)" % (url, str(response.status_code)))
		
        		                	# Public Bucket
                		        	if response.status_code == 200:
                        	        			self.text("+", "Found Bucket: %s (%s)" % (url,str(response.status_code)))
                                				os.system("echo %s >> %s"% (url, args.output))
	
				
					except:
						pass

				        url = ("http://%s%s%s.s3.amazonaws.com" % (bucket, seperator, domain))
                                        if args.quite == "0":
                                                self.text("i", url)
                                        # Try to get the response a check the status_code for a bucket
                                        try:
                                                # make a request
                                                response = requests.get(url, verify=True, timeout=10)
                                                # Access Denied
                                                if response.status_code == 403:
                                                        self.text("!", "Found Bucket: %s (%s)" % (url, str(response.status_code)))

                                                # Public Bucket
                                                if response.status_code == 200:
                                                                self.text("+", "Found Bucket: %s (%s)" % (url,str(response.status_code)))
                                                                os.system("echo %s >> %s"% (url, args.output))
                                                                                                                                                                                                                                                                                                                                                                                                
					except:
                                                pass

				if i == 1:

					url = ("https://%s%s%s.s3.amazonaws.com" % (domain, seperator, bucket))
                                        if args.quite == "0":
                                                self.text("i", url)
                                        # Try to get the response a check the status_code for a bucket
                                        try:
                                                # make a request
                                                response = requests.get(url, verify=True, timeout=10)
                                                # Access Denied
                                                if response.status_code == 403:
                                                        self.text("!", "Found Bucket: %s (%s)" % (url,str(response.status_code)))

                                                # Public Bucket
                                                if response.status_code == 200:
                                                        if "The specified bucket does not exist" in response.text:
                                                                self.text("+", "Found Bucket: %s (%s)" % (url,str(response.status_code)))
                                                                os.system("echo %s >> %s" % (url, args.output))

					except:
						pass


					url = ("http://%s%s%s.s3.amazonaws.com" % (domain, seperator, bucket))
                                        if args.quite == "0":
                                                self.text("i", url)
                                        # Try to get the response a check the status_code for a bucket
                                        try:
                                                # make a request
                                                response = requests.get(url, verify=True, timeout=10)
                                                # Access Denied
                                                if response.status_code == 403:
                                                        self.text("!", "Found Bucket: %s (%s)" % (url,str(response.status_code)))

                                                # Public Bucket
                                                if response.status_code == 200:
                                                        if "The specified bucket does not exist" in response.text:
                                                                self.text("+", "Found Bucket: %s (%s)" % (url,str(response.status_code)))
                                                                os.system("echo %s >> %s" % (url, args.output))

                                        except:
                                                pass
    # Start the scanner
    def scan(self):

        # Validate the arguments
        if (self.args.domains != None):
            if (os.path.isfile(self.args.domains)):
                # Start checking for buckets
                doms = open(self.args.domains, 'r')
		print Style.RESET_ALL + Style.BRIGHT + Fore.CYAN + "Scanning...\n"
                time.sleep(2)
		for domain in doms.readlines():
                    	host = domain.strip()	
			print Style.RESET_ALL + Style.BRIGHT + Fore.CYAN + " Checking " + Fore.GREEN + host + Fore.CYAN+" for buckets.\n" 
			print Style.RESET_ALL + Style.BRIGHT + Fore.WHITE +"------------------------------------------------"
			self.checker(host)			


		if os.path.isfile(args.output):
			print Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + "------------------ FOUND ---------------------"
			buckets = open(args.output, 'r')
			for bucket in buckets.readlines():
				bucket = bucket.strip()
				print bucket
			print "--------------------------------------"
# Print the banner
banner()

# Arguments
parser = argparse.ArgumentParser(description="S3 Bucket Scanner")
parser.add_argument("--domains", "-d", help="The list of domains")
parser.add_argument("--buckets", "-b", help="The file containing the buckets")
parser.add_argument("--quite",   "-q", help="Verbose (1 = false, 0 = true)",default="1")
parser.add_argument("--output",  "-o", help="The output file")
args = parser.parse_args()

# Start the scanner
bucket = Scanner(args)
bucket.scan()

