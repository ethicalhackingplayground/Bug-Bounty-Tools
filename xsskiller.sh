#!/bin/bash

echo -e "\e[1m"
echo -e "\e[34m"
echo """
__   __ _____ _____ _  ___ _ _           
\ \ / // ____/ ____| |/ (_) | |          
 \ V /| (___| (___ | ' / _| | | ___ _ __ 
  > <  \___ \\___ \|  < | | | |/ _ \ '__|
 / . \ ____) |___) | . \| | | |  __/ |   
/_/ \_\_____/_____/|_|\_\_|_|_|\___|_| 
"""

echo -e "\e[1m"
echo -e "\e[94m Do you want to do a new scan [Y/n]: "
read $scans

if [ "$scans" = "Yes" ] || [ "$scans" = "Y" ] || [ "$scans" = "YES" ]; then

	rm *.out
	echo -e "\e[1m"
	echo -e "\e[3m\e[35m[+] Scanning for subdomains, Yeet!! "
	echo -e "\e[32m[+] Could take sometime.."
	echo -e "\e[0m"


	cp bounty-targets-data/data/wildcards.txt .; cat wildcards.txt | sed 's/^*.//g' | grep -v '*' > wildcards_without_stars.txt; 

	while read host; 
   	do file=$host && file+="_subfinder.out"; 
   		~/go/bin/subfinder -o $file -d $host -silent; 

	done < wildcards_without_stars.txt;	
	cat *.out > all_subdomains.lst; 

	echo -e "\e[1m"
	echo -e "\e[3m\e[91m Appending https:// to each subdomain.."
	echo -e "\e[0m"
	while read $file;
	do 
		echo "https://"$h >> subdomins.txt 
	done < all_subdomains.lst;


	xsser -i /root/xsskiller/bounty-targets-data/data/domains.txt --auto --Str --Coo --Xsa --Xsr --Ind --Anchor --Dcp --Dom -c 100 --Cw=50 --delay=1 --save  --Phpids0.6.5  --Phpids0.7 --Imperva --Webknight --F5bigip --Barracuda --Modsec --Quickdefense --heuristic --threads=10 --silent
	echo -e "\e[1m"
	echo -e "\e[93m[+] Running XSS on all <domains>, Yeet!! "
	echo -e "\e[0m"
	
	echo -e "\e[34m\e[5m\e[1mPlease Wait.."
	echo -e "\e[0m"
	xsser -i /root/xsskiller/bounty-targets-data/data/domains.txt --auto --Str --Coo --Xsa --Xsr --Ind --Anchor --Dcp --Dom -c 100 --Cw=50 --delay=1 --save  --Phpids0.6.5  --Phpids0.7 --Imperva --Webknight --F5bigip --Barracuda --Modsec --Quickdefense --heuristic --threads=10 --silent

	echo -e "\e[1m"
	echo -e "\e[93m"
	cat *.raw >> report.raw
	cat report.raw
	echo -e "\e[0m"


else
	
        cat *.out > all_subdomains.lst; 

	echo -e "\e[1m"
	echo -e "\e[3m\e[91m Appending https:// to each subdomain.."
	echo -e "\e[0m"
	while read $file;
	do 
		echo "https://"$h >> subdomins.txt 
	done < all_subdomains.lst;


	xsser -i /root/xsskiller/bounty-targets-data/data/domains.txt --auto --Str --Coo --Xsa --Xsr --Ind --Anchor --Dcp --Dom -c 100 --Cw=50 --delay=1 --save  --Phpids0.6.5  --Phpids0.7 --Imperva --Webknight --F5bigip --Barracuda --Modsec --Quickdefense --heuristic --threads=10 --silent
	echo -e "\e[1m"
	echo -e "\e[93m[+] Running XSS on all <domains>, Yeet!! "
	echo -e "\e[0m"
	
	echo -e "\e[34m\e[5m\e[1mPlease Wait.."
	echo -e "\e[0m"
	xsser -i /root/xsskiller/bounty-targets-data/data/domains.txt --auto --Str --Coo --Xsa --Xsr --Ind --Anchor --Dcp --Dom -c 100 --Cw=50 --delay=1 --save  --Phpids0.6.5  --Phpids0.7 --Imperva --Webknight --F5bigip --Barracuda --Modsec --Quickdefense --heuristic --threads=10 --silent

	echo -e "\e[1m"
	echo -e "\e[93m"
	cat *.raw >> report.raw
	cat report.raw
	echo -e "\e[0m"

fi
