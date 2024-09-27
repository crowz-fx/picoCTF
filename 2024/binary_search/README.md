# Binary Search

## Steps

```bash
wget https://artifacts.picoctf.net/c_atlas/17/challenge.zip && unzip challenge.zip

# jump on box
ssh -p 51922 ctf-player@atlas.picoctf.net

# so it's binary search up to 1000, you can guess by halving your guess each time like below example

```

## Example

```
Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: 500
Lower! Try again.
Enter your guess: 250
Higher! Try again.
Enter your guess: 375
Lower! Try again.
Enter your guess: 325
Higher! Try again.
Enter your guess: 350
Higher! Try again.
Enter your guess: 362
Higher! Try again.
Enter your guess: 369
Higher! Try again.
Enter your guess: 372
Higher! Try again.
Enter your guess: 374
Lower! Try again.
Enter your guess: 373
Congratulations! You guessed the correct number: 373
Here's your flag: picoCTF{g00d_gu355_6dcfb67c}
Connection to atlas.picoctf.net closed.
```

## Flag

```
picoCTF{g00d_gu355_6dcfb67c}
```
