import string
import operator
stri = " "

input_string=raw_input("Enter a decrypted string: ")

capsStr = string.upper(input_string)

letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for char in capsStr:
    if char != ' ':
        if char in letters:
            letterCount[char] += 1
        
# for letter, value in letterCount.items():
#     print("Letter : {0}, Value : {1}".format(letter, value))
# Sorting the dictionary 
sort = sorted(letterCount, key = letterCount.get)

# max letter is the last one in the dictionary
max_letter = sort[len(letterCount)-1]
#second max letter is the second last in the dictionary
secondMax_letter = sort[len(letterCount)-2]

#Getting the rotated number
num = ord('E') - ord(max_letter)

for char in capsStr:
    if char == ',' or char == ' ' or char == '.':
        stri = stri + char
    else:
        asciiValue = ord(char)
        if num > 0:
            asciiValue = asciiValue + num
        else:
            asciiValue = num % asciiValue
        if asciiValue > ord('Z'):
            asciiValue = asciiValue - 26
        elif asciiValue < ord('A'):
            asciiValue = asciiValue + 26
        charValue = chr(asciiValue)
        stri = stri + charValue
print stri.replace("\n", " ")
 
    