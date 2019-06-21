# Bug-Bounty-Tools
Find sub domain take overs and XSS on all domains on hackerone and bugcrowd.

### What Are these tools?
These two scripts automate finding subdomain takeovers and XSS (Crosss-site-scripting) Over all domains in
hackerone and bugcrowd.

### How does XSSKiller Work?
The XSSkiller scripts uses xsser to spider through all domains and check for xss in Cookies,Referer,User-Agent and basically everywhere in the request, it also uses bypass filters.




### How to install
**`chmod +x install.sh`**

**`./install.sh`**

*replace this domains.txt file with the one in the bounty-targets-data/data directory*

### How to run tools
**`chmod +x xsskiller.sh && chmod +x subdomain_killer.sh && chmod autsploit.sh`**

**`./xsskiller`**

**`./subdomain_killer.sh`**

  **or**
**`./autosploit.sh`**


### How to create cron job so the scripts run every 12 hours
**`/etc/init.d/cron start`**

**`crontab -e`**

Append this at the end.

*`42 */12 * * *  /root/Bug-Bounty-Tools/autosploit.sh >> ~/cronjob.log 2>&1`*

Hope you enjoy these shell scripts, happy bug hunting.
