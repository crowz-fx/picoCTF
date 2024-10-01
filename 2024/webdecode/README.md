# WebDecode

## Steps
```bash
# launch instance

# load website - http://titan.picoctf.net:53727/

# open inspect, dig through all files, notice a base64-y looking string, decode and boom
echo "cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMTBmOTM3NmZ9" | base64 -d
```

## Flag
```
picoCTF{web_succ3ssfully_d3c0ded_10f9376f}
```