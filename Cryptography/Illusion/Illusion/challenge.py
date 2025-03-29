import random

def paint(bricks):
    return [((b >> 2) | (b << 6)) & 0xff for b in bricks]

def static(layers):
    return "".join(chr(c) for c in layers)

def cloud(wind):  # Hint: Key generator ;)
    random.seed(404)
    return [random.randint(10, 250) for _ in range(len(wind))]

def shadow(sky, air): 
    return [(ord(sky[i]) ^ ((air[i] + i * 3) & 0xff)) for i in range(len(sky))]

def illusion():
    rain = "CSC25{fake_flag_for_testing}"
    fog = cloud(rain)
    mist = shadow(rain, fog)
    haze = paint(mist)
    print("Skycode:", ''.join([format(x, '02x') for x in haze]))

illusion()
