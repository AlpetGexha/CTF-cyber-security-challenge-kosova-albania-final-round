import random
import base64

def sauce(length):
    r = []
    random.seed(2025)
    for _ in range(length):
        r.append(random.randint(0, 255))
    return r

def reverse_lasagna(encrypted, flavor):
    cooked = base64.b64decode(encrypted)
    original_text = []
    for i in range(len(cooked)):
        b = flavor[i]
        a = cooked[i] ^ (((b << (i % 4)) | (b >> (8 - (i % 4)))) & 0xff)
        original_text.append(chr(a))
    return ''.join(original_text)

# Encrypted output and hint
encrypted_output = "aboiMov66WuF7rvzCKw39Y1QYU4XiAf8r+SAEXS3"

# Decode the encrypted output to determine the correct length for the flavor
decoded_length = len(base64.b64decode(encrypted_output))
flavor = sauce(decoded_length)

# Reverse the lasagna function to find the flag
flag = reverse_lasagna(encrypted_output, flavor)
print("Decrypted Flag:", flag)