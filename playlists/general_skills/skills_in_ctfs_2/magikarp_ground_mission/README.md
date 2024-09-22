# Magikarp Ground Mission

## Steps
```bash
# put pwd into file
sshpass -f pwd.txt ssh -l ctf-player venus.picoctf.net -p 49993

# on the box
cat 1of3.flag.txt
cat instructions-to-2of3.txt
cd /
cat 2of3.flag.txt
cat instructions-to-3of3.txt
cd ~
cat 3of3.flag.txt
```

## Flag
```
picoCTF{xxsh_0ut_0f_\/\/4t3r_3ca613a1}
```
