import hashlib

raw_bytes = b"SCHOFIELD"
digest_indexes = [4, 5, 3, 6, 2, 7, 1, 8]

print("magic: ", end="")
magic = ""
for index in digest_indexes:
    b = hashlib.sha256((raw_bytes)).hexdigest()[index]
    magic += b
    print(b, end="")
print()

print("picoCTF{1n_7h3_|<3y_of_" + magic + "}")
