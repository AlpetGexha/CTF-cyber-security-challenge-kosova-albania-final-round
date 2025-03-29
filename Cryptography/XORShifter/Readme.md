# XOR Shifter

150 points

Another XOR encryption maybe? Looking for a key? Nice try!

We need to decrypt the given hex string using a key generated from a random seed. The key is generated using the same seed as the one used for encryption, so we can replicate the key generation process.

FULL CODE:

```python
import random

def get_key(length):
    random.seed(1337)
    return [random.randint(0, 255) for _ in range(length)]

def decrypt(enc_bytes, key):
    return ''.join([chr(enc_bytes[i] ^ (((key[i] << (i % 8)) | (key[i] >> (8 - (i % 8)))) & 0xff)) for i in range(len(enc_bytes))])

# Read the encrypted hex string
with open('output.txt', 'r') as f:
    hex_str = f.read().strip()

# Convert hex to bytes
enc_bytes = [int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2)]

# Get the key using same seed
key = get_key(len(enc_bytes))

# Decrypt
flag = decrypt(enc_bytes, key)
print(flag)
```

flag:

`CSC25{tHis_i5_tHE_3asY_p4rT}`
