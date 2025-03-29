# Illusion

300 points

Maybe it is not what it seems. Not as easy but not as hard.

### Solution

Seening the challange.py the flag its encrypted "mist", "fog", "haze" and the rain is a flag

So base on that we try to change the order of transformation.

```python
skycode_hex = "d82a0d71c8b9debff65e880977455314b42e15745b2942c3e1"  # the code from output.txt
haze = [int(skycode_hex[i:i+2], 16) for i in range(0, len(skycode_hex), 2)]

# Reverse the transformations
mist = reverse_paint(haze)
fog = reverse_cloud(mist)
flag = reverse_shadow(mist, fog)

print("Recovered flag:", flag)
```

flag:

`CSC25{H3aD_iN_tH3_CIOuDs}`
