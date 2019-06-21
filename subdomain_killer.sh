#!/bin/bash

echo -e "\e[1m"
echo -e "\e[35m"
echo """
  ______       _     _     _ _ _ _              
 / _____)     | |   (_)   | (_) | |             
( (____  _   _| |__  _____| |_| | | _____  ____ 
 \____ \| | | |  _ \|  _   _) | | || ___ |/ ___)
 _____) ) |_| | |_) ) |  \ \| | | || ____| |    
(______/|____/|____/|_|   \_)_|\_)_)_____)_|    
                                               
"""


echo -e "\e[1m"
echo -e "\e[93m[+] Searching for subdomain takeovers.."
echo -e "\e[0m"

cd ~/subdomain_takeover/bounty-targets-data/; 
git pull; 
cd ~/subdomain_takeover; 
cp ~/subdomain_takeover/bounty-targets-data/data/wildcards.txt ./; cat wildcards.txt | sed 's/^*.//g' | grep -v '*' > wildcards_without_stars.txt; 
while read host; 
   do file=$host && file+="_subfinder.out"; 
   ~/go/bin/subfinder -o $file -d $host; 
done < ./wildcards_without_stars.txt;
cat ./*.out > all_subdomains.lst; 
~/go/bin/SubOver -l ./all_subdomains.lst -timeout 5 -o subover.out;
