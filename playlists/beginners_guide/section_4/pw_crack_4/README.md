# PW Crack 4

## Steps
```bash
wget https://artifacts.picoctf.net/c/20/level4.py https://artifacts.picoctf.net/c/20/level4.flag.txt.enc https://artifacts.picoctf.net/c/20/level4.hash.bin
cat level4.py

# see pwds, same as last level loop through, but add grep to reduce output

maybe_pwds=("158f" "1655" "d21e" "4966" "ed69" "1010" "dded" "844c" "40ab" "a948" "156c" "ab7f" "4a5f" "e38c" "ba12" "f7fd" "d780" "4f4d" "5ba1" "96c5" "55b9" "8a67" "d32b" "aa7a" "514b" "e4e1" "1230" "cd19" "d6dd" "b01f" "fd2f" "7587" "86c2" "d7b8" "55a2" "b77c" "7ffe" "4420" "e0ee" "d8fb" "d748" "b0fe" "2a37" "a638" "52db" "51b7" "5526" "40ed" "5356" "6ad4" "2ddd" "177d" "84ae" "cf88" "97a3" "17ad" "7124" "eff2" "e373" "c974" "7689" "b8b2" "e899" "d042" "47d9" "cca9" "ab2a" "de77" "4654" "9ecb" "ab6e" "bb8e" "b76b" "d661" "63f8" "7095" "567e" "b837" "2b80" "ad4f" "c514" "ffa4" "fc37" "7254" "b48b" "d38b" "a02b" "ec6c" "eacc" "8b70" "b03e" "1b36" "81ff" "77e4" "dbe6" "59d9" "fd6a" "5653" "8b95" "d0e5")
for maybe_pwd in "${maybe_pwds[@]}"; do \
  echo $maybe_pwd | python level4.py | grep pico
done

```

## Flag
```
picoCTF{fl45h_5pr1ng1ng_cf341ff1}
```
