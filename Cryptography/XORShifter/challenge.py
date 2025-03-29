import random

f = "CSC25{fake_flag_for_testing}"
s = 1337

def k(x):
    random.seed(s)
    return [random.randint(0, 255) for _ in range(x)]

def x(d, j):
    return [(ord(d[i]) ^ (((j[i] << (i % 8)) | (j[i] >> (8 - (i % 8)))) & 0xff)) for i in range(len(d))]

def m():
    j = k(len(f))
    c = x(f, j)
    print(''.join([f"{i:02x}" for i in c]))

m()
