# Enhance

## Steps
```bash
wget https://artifacts.picoctf.net/c/102/drawing.flag.svg
file drawing.flag.svg

strings drawing.flag.svg

# see the flag is broke into multiple tspan elements, so use perl extended grep to capture and format into one word
strings drawing.flag.svg | grep -Po '(?<=>)(.*)(?=</tspan)' | tr -d ' \n' > flag.txt
```

## Flag
```
picoCTF{3nh4nc3d_d0a757bf}
```
