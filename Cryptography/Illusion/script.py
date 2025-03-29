import random

def reverse_paint(haze):
    return [((b << 2) | (b >> 6)) & 0xff for b in haze]

def reverse_shadow(mist, fog):
    return ''.join(chr(mist[i] ^ ((fog[i] + i * 3) & 0xff)) for i in range(len(mist)))

def reverse_cloud(fog):
    random.seed(404)
    return [random.randint(10, 250) for _ in range(len(fog))]

skycode_hex = "d82a0d71c8b9debff65e880977455314b42e15745b2942c3e1"  # the code from output.txt
haze = [int(skycode_hex[i:i+2], 16) for i in range(0, len(skycode_hex), 2)]

# Reverse the transformations
mist = reverse_paint(haze)
fog = reverse_cloud(mist)
flag = reverse_shadow(mist, fog)

print("Recovered flag:", flag)