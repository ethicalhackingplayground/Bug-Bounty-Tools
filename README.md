# Bug-Bounty-Tools
These are all the tools I have programmed to help me with bugbountys

## Examples of usage:

### Open Redirects

```
python redir.py -w urls.txt -p payloads -d evil.com -s 0 -o openredirects.txt
```

![Screenshot](open_redirect.jpg)

### Local File inclusion

```
python lfi.py -u urls.txt -p payloads -t 100 -o lfi.txt
```

![Screenshot](lfitester.PNG)

### SSRF Links

```
python find_urls2.py -d domain.com -t 100 -s urls.txt -o links.txt
```

```
python find_urls2.py -d domain.com -t 100 -s source.js -o links.txt
```

### CRLF 

```
python crlf-auto.py -f urls.txt
```

### S3 Buckets

```
python s3bucketer.py -d urls.txt -b buckets.txt -q 1 -o found.txt
```

![Screenshot](s3bucketer2.PNG)

Note, automation tools should be the last resort because devlopers would use such tools during there testing.

Enjoy hunters,

If you find something and you enjoy my tools

Donate to me here.

<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/users/EthicalHackingPlayground/sponsorship" data-color-scheme="no-preference: dark; light: dark; dark: dark;" data-icon="octicon-heart" data-size="large" aria-label="Sponsor @EthicalHackingPlayground on GitHub">Sponsor</a>
