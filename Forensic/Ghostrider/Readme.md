# Ghost Rider

300

A company has been compromised. Our blue team has provided the apache logs. Can you find the request where the attackers dropped a beacon? Maybe check for GET requests ;)

### Solution

On line 820

```
4.53.215.180 - - [26/Mar/2025:15:17:10 +0100] "GET /tinyurl.com/3ant4vc2 HTTP/1.0" 200 24964
```

We have this https://pastebin.com/raw/Fx0y5fSu with give us the flag

flag:

`CSC25{ApT_99_1s_uPOn_uS !!! }`
