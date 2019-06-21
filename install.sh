#!/bin/bash

echo -e "\e[1m"
echo -e "\e[32m[+] Acquiring Targets.."
echo -e "\e[0m"
git clone https://github.com/arkadiyt/bounty-targets-data;

echo -e "\e[1m"
echo -e "\e[32m[+] Installing Xsser"
echo -e "\e[0m"
apt-get install xsser

echo -e "\e[1m"
echo -e "\e[32m[+] Downloading sunfinder.."
echo -e "\e[0m"

apt install golang;
go get github.com/subfinder/subfinder;


