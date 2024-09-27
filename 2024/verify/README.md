# Verify

## Steps

```bash
# spin up instance
wget https://artifacts.picoctf.net/c_rhea/20/challenge.zip
unzip challenge.zip

# check checksum exists
grep -r 'fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7'

# go through every file running the sha256
find home/ctf-player/drop-in/files -type f -exec sha256sum {} + | grep $(cat home/ctf-player/drop-in/checksum.txt) | awk '{print $2}'

# run the decrypt on the box as they hardcoded /home lol
ssh -p 52987 ctf-player@rhea.picoctf.net

./decrypt.sh $(find files -type f -exec sha256sum {} + | grep $(cat checksum.txt) | awk '{print $2}')
```

## Flag

```
picoCTF{trust_but_verify_87590c24}
```
