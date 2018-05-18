import string
import random

# str = raw_input("Enter a string: ")
# key = input("Input Shift Distance: ")
#
# capsStr = string.upper(str)
#
# for char in capsStr:
#     if char != ' ':
#         asciiValue = ord(char)
#         if key > 0:
#             asciiValue = asciiValue + key
#         else:
#             asciiValue = key % asciiValue
#         if asciiValue > ord('Z'):
#             asciiValue = asciiValue - 26
#         charValue = chr(asciiValue)
#         print charValue,

str = raw_input("Enter a string: ")
method = raw_input("Enter 'E' for Encryption or 'D' for Decryption: " )
key = input("Enter random seed: ")

capsStr = string.upper(str)

a = 7
c = 11
m = 26

random.seed(key)
x = random.randint(1,10)

if method == "e":
    for char in capsStr:
        if char != " ":
            asciiValue = ord(char) + x
            x = (a * x + c) % m
        if asciiValue > ord('Z'):
            asciiValue = asciiValue - 26
        charValue = chr(asciiValue)
        print charValue,
        
if method == "d":
    for char in capsStr:
        if char != " ":
            asciiV = ord(char) - x
            x = (a * x + c) % m
        if asciiV < ord('A'):
            asciiV = asciiV + 26
        charV = chr(asciiV)
        print charV,