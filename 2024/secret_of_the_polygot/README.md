# Secret of the Polygot

## Steps
```bash
wget https://artifacts.picoctf.net/c_titan/7/flag2of2-final.pdf

# run file, strings and exiftool to try to get some metadata
file flag2of2-final.pdf
strings flag2of2-final.pdf
exiftool flag2of2-final.pdf 

# see the 'created in GIMP' comment and the warning '[minor] Trailer data after PNG IEND chunk'
# open in gimp, see the first half of the flag

# look for the IEND in hex using xxd, -C is context in grep so add two lines before and after
xxd flag2of2-final.pdf | grep -C 2 "IEND"

# found this awesome collection of file signatures, see PDF is 25 50 44 46
# https://www.garykessler.net/library/file_sigs.html


# throw the hex into a hex viewer, trim by leave the PDF header till end of file, save, export
# run file, determine it's a pdf, open, get 2nd half of flag

xxd -r pdf_hex > pdf_binary
file pdf_binary

cp pdf_binary > embedded.pdf
```

## Flag
```
picoCTF{f1u3n7_1n_pn9_&_pdf_53b741d6}
```