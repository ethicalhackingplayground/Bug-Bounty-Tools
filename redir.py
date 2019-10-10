#!/usr/bin/env python
import json
import requests
import sys
import time
import os
import argparse
import urlparse
from bs4 import BeautifulSoup
from colorama import Style,Fore

common_params = ["/", "next", "url", "target", "rurl", "dest", "destination",
                 "redir", "redirect_url", "redirect_uri", "redirect", "redirect.cgi?", "/out/",
                 "view", "/login/?to", "image_url", "go", "return", "returnTo", "return_to", "checkout_url",
                 "continue", "return_path", "returnUrl", "goto", "continue_to", "redirect"]

top = Style.BRIGHT + Fore.BLUE + """
 ########################################
 #                                      #
 #       _                              #
 #      |_)  _   _| o ._ _   _ _|_      #
 #      | \ (/_ (_| | | (/_ (_  |_      #
 #                                      #
 #                                      #
 #               @z0idex                #
 ########################################
    """ + Style.RESET_ALL

def main():
    os.system('clear')

    print(top)

    parser = argparse.ArgumentParser()

    parser.add_argument('-w', help='path to file of domain list', nargs=1, dest='domain', required=True)
    parser.add_argument('-p', help='payload wordlist', nargs=1, dest='payload', required=True)
    parser.add_argument('-d', help="destination host", nargs=1, dest='destination', required=True)
    parser.add_argument('-s', help="spider through sites", nargs=1, dest='spider', required=True)
    parser.add_argument('-o', help='output to file', nargs=1, dest='output', required=True)
    args = parser.parse_args()

    spider = args.spider[0]

    # first argument - file with subdomains
    file = args.domain[0]

    # second argument - payload string
    payloads = args.payload[0]

    # The final destination
    dest = str(args.destination[0])

    # Output file
    output = str(args.output[0])


    #open file with subdomains and iterates
    with open(file) as f:

                print ""
                print Style.BRIGHT + Fore.MAGENTA + "Searching for open redirects, prayz to the lordz.."
                print "\n"
                time.sleep(4)

		redirects = list()

                # loop for find the trace of all requests (303 is an open redirect) see the final destination
		if spider == '0':
                        for host in f:
                                with open(payloads) as p:
                                        for payload in p:


                                                        # strip some stuff
                                                        url = host.strip()
                                                        payload = payload.strip()


                                                        # replace the wildcard with the destination
                                                        payload = payload.replace("*", str(dest))



                                                        # find the parameters in the url
                                                        params = urlparse.parse_qs(urlparse.urlparse(url).query)
                                                        if len(params) == 0:
                                                                url = url + payload
                                                        else:
                                                                for p in params:
                                                                        if p in common_params:
                                                                                print Fore.WHITE + "--------------------------"
                                                                                print Fore.GREEN + "Potential VULN Parameter %s" %p
                                                                                print Fore.WHITE + "--------------------------"
                                                                                p=url.replace(p,("%s=%s" % (p, dest)))
                                                                                url=p



                                                        try:
								
                                                                print Style.BRIGHT + Fore.WHITE + "[ " + Fore.YELLOW + "CHECKING" + Fore.WHITE + " ] " + Fore.WHITE + url    
								response = requests.get(url, allow_redirects=True)                                                                                                                           
                                                                # check the status code
                                                                if len(response.history) != 0:

                                                                        # check to see if there is an open redirect
                                                                        d1 = "https://" + dest
                                                                        s2 = "http://" + dest
                                                                        if response.url == d1 or response.url == d2:

                                                                                print Style.BRIGHT + Fore.WHITE + "[ " + Fore.GREEN + "FOUND" + Fore.WHITE + " ] " + Fore.YELLOW + "Open Redirect, Request was redirected"
                                                                                print Style.BRIGHT + Fore.CYAN + "[Dest] " + Fore.WHITE + response.url
                                    
										os.system("echo %s >> %s" % (url, output))
                                                        except:
                                                                pass
 
                        print Style.BRIGHT + Fore.GREEN + "\n --------------------------- RESULTS ------------------------\n"
			if os.path.isfile(output):
				results = open(output, 'r')
				for result in results.readlines():
					print Fore.GREEN + result
			else:
				print Fore.RED + "No Results.."

                else:
                        print Style.BRIGHT + Fore.CYAN + "\nStarting Spider...\n"

                        for host in f:

                                # strip some stuff
                                host = host.strip()                
				try:
					r = requests.get(host)
					data = r.text
        	                        soup = BeautifulSoup(data, "lxml")
                	                payloadFile = open(payloads).readlines()
	
        	                        crawled_urls = []
                	                for link in soup.find_all('a'):
                        	        	ref = link.get('href')
                                	    	if "https://" in ref or "http://" in ref:
                                        		crawled_urls.append(ref)
                                	for url in crawled_urls:

                           	        	payloadFile = open(payloads)
                                    		for payload in payloadFile.readlines():

                                            		payload = payload.strip()
                                            		# replace the wildcard with the destination
                                            		payload = payload.replace("*", str(dest))



                                            		# find the parameters in the url
                                            		params = urlparse.parse_qs(urlparse.urlparse(url).query)

                                            		if len(params) == 0:
                                                 		website = url + payload

                                            		else:
                                                		for p in params:
                                                    			if p in common_params:
                                                        			print Fore.WHITE + "--------------------------"
                                                        			print Fore.GREEN + "Potential VULN Parameter %s" %p
                                                        			print Fore.WHITE + "--------------------------"
                                                        			p=website.replace(p,("%s=%s" % (p, dest)))
                                                        			website=p

                               
							try:
                                            			print Style.BRIGHT + Fore.WHITE + "[ " + Fore.YELLOW + "CHECKING" + Fore.WHITE + " ] " + Fore.WHITE + website
                                       
  								response = requests.get(website, allow_redirects=True)

                                            			# check the status code
                                            			if len(response.history) != 0:

                                                			# check to see if there is an open redirect
                                                    			d1 = "https://" + dest
                                                    			d2 = "http://" + dest
                                                    			if response.url == d1 or response.url == d2:

                                                        			print Style.BRIGHT + Fore.WHITE + "[ " + Fore.GREEN + "FOUND" + Fore.WHITE + " ] " + Fore.YELLOW + "Open Redirect, Request was redirected"
                                                        			print Style.BRIGHT + Fore.CYAN + "[Dest] " + Fore.WHITE + response.url
                                                        			os.system("echo %s >> %s" % (url, output))
							except:
								pass
                                except:	
					pass 
                 	print Style.BRIGHT + Fore.GREEN + "\n --------------------------- RESULTS ------------------------\n"
                        if os.path.isfile(output):
                                results = open(output, 'r')
                                for result in results.readlines():
                                        print Fore.GREEN + result
                        else:
                                print Fore.RED + "No Results.."        
                            

main()
