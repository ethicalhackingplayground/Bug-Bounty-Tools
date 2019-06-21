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
echo -e "\e[93m[+] Running XSS on all domains, Yeet!! "
echo -e "\e[0m"

echo -e "\e[34m\e[5m\e[1mPlease Wait.."
echo -e "\e[0m"
xsser -i /root/xsskiller/bounty-targets-data/data/domains.txt --auto --Str --Coo --Xsa --Xsr --Ind --Anchor --Dcp --Dom -c 100 --Cw=10 --delay=1 --save  --Phpids0.6.5  --Phpids0.7 --Imperva --Webknight --F5bigip --Barracuda --Modsec --Quickdefense --heuristic --threads=10 --silent
