# Secret

300 Points

### Description

You've stumbled upon a mysterious program that greets the world but seems to hide something deeper.

### Solution

Using ghidra to analyze the binary, we found the secret function

```c#
void secret_function(void)

{
  char local_78 [31];
  undefined local_59;
  undefined8 local_58;
  undefined8 local_50;
  undefined8 local_48;
  undefined8 local_40;
  char *local_38;
  char *local_30;
  char *local_28;
  char *local_20;
  undefined1 *local_18;
  char *local_10;

  local_58 = 0x3866733d3a4b5b4b;
  local_50 = 0x6b6d7b57677b577c;
  local_48 = 0x3b7c6e69577c6d7a;
  local_40 = 0xb7cb7564643c577a;
  local_10 = aa_bb((char *)&local_58,0xaa);
  local_18 = aa_bb(local_10,0x55);
  puts("You found the secret function!");
  fflush(stdout);
  local_20 = aa_bb((char *)&local_58,0x78);
  local_28 = aa_bb(local_20,0x56);
  local_30 = aa_bb(local_28,0x34);
  local_38 = aa_bb(local_30,0x12);
  local_59 = 0;
  strcpy(local_78,local_38);
  printf("Congratulations! Flag: %s\n",local_38);
  return;
}
```

SO base on that we can make a script but first lets get the combined byte

```c#
local_58 = 0x3866733d3a4b5b4b; // Bytes: 4B 5B 4B 3A 3D 73 66 38
local_50 = 0x6b6d7b57677b577c; // Bytes: 7C 57 7B 67 7B 57 6D 6B
local_48 = 0x3b7c6e69577c6d7a; // Bytes: 7A 6D 7C 57 69 6E 7C 3B
local_40 = 0xb7cb7564643c577a; // Bytes: 7A 57 3C 64 64 75 CB B7

final_bit = "4B5B4B3A3D7366387C577B677B576D6B7A6D7C57696E7C3B7A573C646475CBB7";
```

```python
encoded_bytes = bytes.fromhex(
    "4B5B4B3A3D7366387C577B677B576D6B7A6D7C57696E7C3B7A573C646475CBB7"
)

step1 = bytes([b ^ 0x78 for b in encoded_bytes])
step2 = bytes([b ^ 0x56 for b in step1])
step3 = bytes([b ^ 0x34 for b in step2])
flag_bytes = bytes([b ^ 0x12 for b in step3])

flag = flag_bytes.decode('utf-8', errors='ignore').split('\x00')[0]
print("Flag:", flag)
```

flag:
`CSC25{n0t_so_secret_aft3r_4ll}`
