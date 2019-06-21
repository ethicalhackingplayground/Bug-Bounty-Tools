#!/bin/bash

echo -e "\e[1m"
echo -e "\e[32m[+] Acquiring Targets.."
echo -e "\e[0m"
cd ~;
git clone https://github.com/arkadiyt/bounty-targets-data;

echo -e "\e[1m"
echo -e "\e[32m[+] Downloading subfinder.."
echo -e "\e[0m"

apt install golang;
go get github.com/subfinder/subfinder;

echo -e "\e[1m"
echo -e "\e[32m[+] Downloading SubOver.."
echo -e "\e[0m"

go get github.com/Ice3man543/SubOver

