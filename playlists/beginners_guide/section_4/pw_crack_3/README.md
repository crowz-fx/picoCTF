# PW Crack 3

## Steps
```bash
wget https://artifacts.picoctf.net/c/18/level3.py https://artifacts.picoctf.net/c/18/level3.flag.txt.enc https://artifacts.picoctf.net/c/18/level3.hash.bin
cat level3.py
# see potential pwds, create a for loop to pipe it into the script

pwds=("8799" "d3ab" "1ea2" "acaf" "2295" "a9de" "6f3d")
for maybe_pwd in "${pwds[@]}"; do \
  echo $maybe_pwd; \
  echo $maybe_pwd | python level3.py 
done

# in the output the correct pwd will show
```

## Flag
```
picoCTF{m45h_fl1ng1ng_6f98a49f}
```
