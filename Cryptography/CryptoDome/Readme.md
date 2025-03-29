# CryptoDome

### Description

300 points

The bank is using a strong encryption mechanism. Try to break the logic of the new encryption.

### Soulution

...

We reverse the lasagna (we swap a with b)

```python
def reverse_lasagna(encrypted, flavor):
    cooked = base64.b64decode(encrypted)
    original_text = []
    for i in range(len(cooked)):
        b = flavor[i]
        a = cooked[i] ^ (((b << (i % 4)) | (b >> (8 - (i % 4)))) & 0xff)
        original_text.append(chr(a))
    return ''.join(original_text)
```

and we just call on this order

```python
encrypted_output = "aboiMov66WuF7rvzCKw39Y1QYU4XiAf8r+SAEXS3"

decoded_length = len(base64.b64decode(encrypted_output))
flavor = sauce(decoded_length)

flag = reverse_lasagna(encrypted_output, flavor)
print("Decrypted Flag:", flag)
```

FLAG:

`CSC25{0bFusC4t4d_bY_tH3_d3ViL}`
