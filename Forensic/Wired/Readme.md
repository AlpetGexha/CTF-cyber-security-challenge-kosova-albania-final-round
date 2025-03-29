# Wired

300 Points

Check the wire first and then automate it.

### Solution

on the automation.ps1 this a logic that convert 2 string to base64

```powershell
$X1 = "aHR0cHM6Ly9wYXN0ZWJpbi5jb20v"; $X2 = "amIyVU5hNko="
$U = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($X1 + $X2))
```

`aHR0cHM6Ly9wYXN0ZWJpbi5jb20vamIyVU5hNko=` is the base64 of `https://pastebin.com/jb2UNa6J`

flag:

`CSC25{H1dd3n_iN_tH3_W1r3}`
