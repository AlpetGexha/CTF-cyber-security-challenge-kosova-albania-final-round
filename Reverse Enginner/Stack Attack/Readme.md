# Stack Attack

450 points

### Description

Can you analyze the stack, break through the security measures, and retrieve the flag?

### Solution

using ghidra to analyze the binary we gon the .rawdata and we see the secret function and we try to reverseit with xor and we get the flag

```c#
void secret_function(void)

{
  undefined auStack_78 [31];
  undefined uStack_59;
  undefined8 uStack_58;
  undefined8 uStack_50;
  undefined8 uStack_48;
  undefined8 uStack_40;
  undefined8 uStack_38;
  undefined8 uStack_30;
  undefined8 uStack_28;
  undefined8 uStack_20;
  undefined8 uStack_18;
  undefined8 uStack_10;

  uStack_58 = 0x3866733d3a4b5b4b;
  uStack_50 = 0x6b6d7b57677b577c;
  uStack_48 = 0x3b7c6e69577c6d7a;
  uStack_40 = 0xb7cb7564643c577a;
  uStack_10 = aa_bb(&uStack_58,0xffffffaa);
  uStack_18 = aa_bb(uStack_10,0x55);
  func_0x00101040(&UNK_00102008);
  func_0x00101070(stdout);
  uStack_20 = aa_bb(&uStack_58,0x78);
  uStack_28 = aa_bb(uStack_20,0x56);
  uStack_30 = aa_bb(uStack_28,0x34);
  uStack_38 = aa_bb(uStack_30,0x12);
  uStack_59 = 0;
  func_0x00101030(auStack_78,uStack_38);
  func_0x00101060(&UNK_00102027,uStack_38);
  return;
}
```

```python
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
```

flag:

`CSC25{cr4ck_th4t_c0de_buff3r_overfl0w}`
