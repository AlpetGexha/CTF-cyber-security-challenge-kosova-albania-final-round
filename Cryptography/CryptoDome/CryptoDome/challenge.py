import random
import base64

def spaghetti(x):
    return sum([ord(c) for c in "ThisIsWrong!!!"]) % x

def cheese(z):
    w = []
    for h in z:
        w.append(((h << 3) & 0xff) | (h >> 5))
    return w

def sauce(s):
    r = []
    random.seed(2025)
    for _ in range(len(s)):
        r.append(random.randint(0, 255))
    return r

def lasagna(text, flavor):
    cooked = []
    for i in range(len(text)):
        a = ord(text[i])
        b = flavor[i]
        cooked.append((a ^ ((b << (i % 4)) | (b >> (8 - (i % 4)))) & 0xff))
    return base64.b64encode(bytes(cooked)).decode()

def main():
    hint = "you will need to reverse the recipe"
    code = "CSC25{fake_flag_for_testing}"
    spice = sauce(code)
    dish = lasagna(code, spice)
    print("Encrypted Output:", dish)
    print("Hint:", hint)

main()
