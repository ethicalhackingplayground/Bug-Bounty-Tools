[[ -s "$HOME/.profile" ]] && source "$HOME/.profile" # Load the default .profile
[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm" # Load RVM into a shell session *as a function*


sfinder() {
for i in `cat $1`
do
subfinder -b -d $i -v -t 200 -w /home/z0id/all.txt -o "$i-001".txt  -t 1000
done
}

bf() {
python /home/z0id/BurpFeed/bfeed-threaded.py $1 $2
}


s3takeover() {
clear
for i in `cat $1`
do
http -b GET $i | grep -E -q '<Code>NoSuchBucket</Code>|<li>Code: NoSuchBucket</li>' && echo -e "\e[1;97m[$i] - \e[1;32m[BINGO] Subdomain takeover may be possible" >> takeovers.txt || echo -e "\e[1;97m[$i] - \e[2;31mSubdomain takeover is not possible" 
done
}

screenshots() {
sudo eyewitness -f $1 -d /mnt/c/Users/Blake/Desktop/$2 --web --threads 30
}

redirects() {
cd /home/z0id/z0idstools/;
python redir.py -w $1 -d evil.com -p payloads -o $2 -s 0
}

s3buckets() {
cd /home/z0id/z0idstools/s3Bucketer/;
python s3bucketer.py -d sites -b buckets.txt -o $1 -q 1 
}

sjack() {
subjack -w $1 -a -ssl -v 
}

afinder() {
assetfinder -subs-only $1 | tee -a $1.txt
}

reconpad() {
cd /home/z0id/recon
}

sinks() {
grep -m 10 --color -HnrE "/after\\(|\\.append\\(|\\.before\\(|\\.html\\(|\\.prepend\\(|\\.replaceWith\\(|\\.wrap\\(|\\.wrapAll\\(|\\$\\(|\\.globalEv[-] Searching now in DNSdumpster..                                                                                               │al\\(|\\.add\\(|jQUery\\(|\\$\\(|\\.parseHTML\\(/" .  $1
}

sp() {
source ~/.bash_profile
}

profile() {
nano ~/.bash_profile
}


fdlist() {
while IFS= read -r host ; do /home/z0id/findomain-linux --output txt --target $host; done < $1
}

fd() {
cd /home/z0id; ./findomain-linux --output txt --target $1
}


oscan() {
python /home/z0id/z0idstools/redirect.py -w $1 -p /home/z0id/z0idtools/redirections -d evil.com
}


ascanlist() {
for i in `cat $1`
do
	ascan $i
done
}

ascan() {
sudo aquatone-discover --domain $1 --threads 30;
sudo aquatone-scan --domain $1 --ports large --threads 30;
sudo aquatone-gather --domain $1 --threads 30;
sudo aquatone-takeover --domain $1 --threads 30;
}

folder() {
mkdir /home/z0id/recon/$1
}

sublist() {
python /home/z0id/tools/Sublist3r/sublist3r.py -d $1 -o $2
}

apiscan() {
while IFS= read -r line; do cd /home/z0id/Astra/; python astra.py -u "$line" --method $2; done < $1
}

hgrip(){ 
history | grep $1
}

pscan() {
python3 /home/z0id/Arjun/arjun.py  -u $1 --get --post -f /home/z0id/Arjun/db/params.txt -o $2 -d 5 -t 1
}

pscanlist() {
python3 /home/z0id/Arjun/arjun.py  --urls $1 --get --post -f /home/z0id/Arjun/db/params.txt -o  $2 -d 5 -t 1
}

#----- AWS -------

s3ls(){
aws s3 ls s3://$1
}

s3cp(){
aws s3 cp $2 s3://$1 
}

#----- misc -----
certspotter(){
curl -s https://certspotter.com/api/v0/certs\?domain\=$1 | jq '.[].dns_names[]' | sed 's/\"//g' | sed 's/\*\.//g' | sort -u | grep $1
} #h/t Michiel Prins

crtsh(){
curl -s https://crt.sh/\?q\=\%25.$1\&output\=json | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u | tee -a $1.txt
}


certnmap(){
curl https://certspotter.com/api/v0/certs\?domain\=$1 | jq '.[].dns_names[]' | sed 's/\"//g' | sed 's/\*\.//g' | sort -u | grep $1  | nmap -T5 -Pn -sS -i - -$
} #h/t Jobert Abma

certbrute(){
cat $1.txt | while read line; do python3 dirsearch.py -e . -u "https://$line"; done
}

ipinfo(){
curl http://ipinfo.io/$1
}

#------ Tools ------
dirsearch(){
python3 /home/z0id/tools/dirsearch/dirsearch.py -e . -u $1 -b
}


knock(){
cd /home/tools/knock/knockpy
python knockpy.py -w list.txt $1
}

ncx(){
nc -l -n -vv -p $1 -k
}
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
source $GOPATH/src/github.com/tomnomnom/gf/gf-completion.bash
