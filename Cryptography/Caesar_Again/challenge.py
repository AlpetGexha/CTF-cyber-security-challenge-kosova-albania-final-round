import string

class O:
    def __init__(self, a):
        self.__key = a
        self.__alpha = string.ascii_lowercase + string.digits

    def __sH(self, c, b):
        if c in self.__alpha:
            return self.__alpha[(self.__alpha.index(c) + b) % len(self.__alpha)]
        else:
            return c

    def Y(self, Z):
        return ''.join(self.__sH(c, self.__key) for c in Z)

    def X(self, W):
        return ''.join(self.__sH(c, -self.__key) for c in W)


def h0RzE5G(dL8rY):
    P = O(7)
    uL5dQ9 = P.Y("CSC25{G1v3_c4eS4r_wHat_b3l0nGs}")
    return uL5dQ9


if __name__ == "__main__":
    m0oZ = h0RzE5G("hidden_string")
    print(f"Encrypted Message: {m0oZ}")
