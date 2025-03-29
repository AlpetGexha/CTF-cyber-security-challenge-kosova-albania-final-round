import struct

def aa_bb(data, xor_val):
    return bytes([b ^ xor_val for b in data])

data = b''
data += struct.pack('<Q', 0x7a6b733d3a4b5b4b)  # local_58
data += struct.pack('<Q', 0x7c3c607c57636b3c)  # local_50
data += struct.pack('<Q', 0x7d6a576d6c386b57)  # local_48
data += struct.pack('<Q', 0x000067577a3b6e6e)[:6]  
data += struct.pack('<H', 0x6d7e)              
data += struct.pack('<Q', 0x0000757f38646e7a)[:6]  


flag_data = aa_bb(data, 0x12)
flag_data = aa_bb(flag_data, 0x34)
flag_data = aa_bb(flag_data, 0x56)
flag_data = aa_bb(flag_data, 0x78)

print("Flag:", flag_data.decode())