# Format String 0

## Steps
```bash

wget https://artifacts.picoctf.net/c_mimas/76/format-string-0 https://artifacts.picoctf.net/c_mimas/76/format-string-0.c

# connect to instance, see it wants options
nc mimas.picoctf.net 61100

# using format specifiers you can essentially tokenise, chose the most 'complex'
# Gr%114d_Cheese - %
# Cla%sic_Che%s%steak %s = string

```

## Flag
```
picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_63191ce6}
```