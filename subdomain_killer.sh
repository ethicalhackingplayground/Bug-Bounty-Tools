#!/bin/bash

echo -e "\e[1m"
echo -e "\e[31m"
echo """
  ______       _     _     _ _ _ _              
 / _____)     | |   (_)   | (_) | |             
( (____  _   _| |__  _____| |_| | | _____  ____ 
 \____ \| | | |  _ \|  _   _) | | || ___ |/ ___)
 _____) ) |_| | |_) ) |  \ \| | | || ____| |    
(______/|____/|____/|_|   \_)_|\_)_)_____)_|    
                                               
"""


echo -e "\e[1m"
echo -e "\e[93m\e[3m[+] Scanning for subdomains, Yeet!!!"
echo -e "\e[95m\e[3m[+] Could take sometime.."
echo -e "\e[0m"

cd ~/subdomain_takeover/bounty-targets-data/; 
git pull; 
cd ~/subdomain_takeover; 
cp ~/subdomain_takeover/bounty-targets-data/data/wildcards.txt ./; cat wildcards.txt | sed 's/^*.//g' | grep -v '*' > wildcards_without_stars.txt; 
while read host; 
   do file=$host && file+="_subfinder.out"; 
   ~/go/bin/subfinder -o $file -d $host -silent; 
done < ./wildcards_without_stars.txt;
cat ./*.out > all_subdomains.lst; 

echo -e "\e[1m"
echo -e "\[93 [+] Finding Subdomain takeovers.."
~/go/bin/SubOver -l ./all_subdomains.lst -timeout 5 -o subover.out;

echo -e "\e[1m"
echo -e "\e[93m"
cat subover.out
