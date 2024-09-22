# Static Ain't Always Noise

## Steps
```bash
wget https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/static https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/ltdis.sh

# look at ltdis.sh script
chmod +x ltdis.sh
./ltdis.sh static

cat static.ltdis.x86_64.txt
cat *.strings.txt | grep pico
```

## Flag
```
picoCTF{d15a5m_t34s3r_f5aeda17}
```
