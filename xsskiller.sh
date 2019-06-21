#!/bin/bash

echo -e "\e[1m"
echo -e "\e[93m[+] Running XSS on all domains, Yeet!! "
echo -e "\e[0m"

xsser -i /root/xsskiller/bounty-targets-data/data/domains.txt --auto --Str --Coo --Xsa --Xsr --Ind --Anchor --Dcp --Dom -c 100 --Cw=10 --save 
