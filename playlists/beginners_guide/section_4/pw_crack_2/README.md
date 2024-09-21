# PW Crack 2

## Steps
```bash
wget https://artifacts.picoctf.net/c/14/level2.py https://artifacts.picoctf.net/c/14/level2.flag.txt.enc
cat level2.py
# see pwd is hex values, copy string, use python to gen pwd in base10
python -c "print(chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39))"
python level2.py
```

## Flag
```
picoCTF{tr45h_51ng1ng_9701e681}
```
