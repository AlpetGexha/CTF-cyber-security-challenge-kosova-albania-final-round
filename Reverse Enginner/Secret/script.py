# Combined bytes (little-endian order)
encoded_bytes = bytes.fromhex(
    "4B5B4B3A3D7366387C577B677B576D6B7A6D7C57696E7C3B7A573C646475CBB7"
)

# XOR with 0x78
step1 = bytes([b ^ 0x78 for b in encoded_bytes])

# XOR with 0x56
step2 = bytes([b ^ 0x56 for b in step1])

# XOR with 0x34
step3 = bytes([b ^ 0x34 for b in step2])

# XOR with 0x12
flag_bytes = bytes([b ^ 0x12 for b in step3])

# Convert to ASCII (stop at first null byte if any)
flag = flag_bytes.decode('utf-8', errors='ignore').split('\x00')[0]
print("Flag:", flag)