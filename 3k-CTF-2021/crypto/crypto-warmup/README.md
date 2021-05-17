# Crypto-warmup

Author: [Krishap-s](https://github.com/Krishap-s)

##Brief Description:

- Decryption of flag by bruteforce

## Requirements:

- Knowledge of python

## Source:

- [Challenge Script](assets/challenge-9117504dc1ed3a5ffe385f8a736c42e384d707e4.py)

- [Decryption Script](assets/decrypt.py)

## Exploitation:

- The original challenge script encrypts our flag to a series of numbers

- The script also has a array of numbers and series of numbers in its comments

- The function ``` make_stuff() ``` is generates a list of random 24 numbers , and the array of numbers in the comments is also 24 numbers long, so it is safe to assume the array is the list of numbers generated during encryption of flag

- Then the numbers after the array is the series of numbers outputed by the program

- The function ``` weird_function1() ``` takes a string and converts each character of the string to an array of lenght 8 containing 0's and 1's  and concatenates the generated from each character

- The array of 0's and 1's is unique to each ascii character

- The function ```do_stuff()``` :
1) takes a 3 character string and uses ```weird_function1()``` to generate an array of 0's and 1's of length 24 (3 characters x 8) , 
2) then zips the randomly generated 24 number array with the array generated from ```weird_function1()```
3) then for each pair of the zip, it multiplies the key of the zip (array of 0's and 1's) with the value (randomly generated 24 number array)
4) then finally sums all the products and returns it

- By trying all 3 character permutations of ascii characters with ```do_stuff()``` and comparing with the series of numbers given in the comments we can bruteforce the flag

## Flag:
```CTF{w4rmup-kn4ps4ck-ftw!}``` 
