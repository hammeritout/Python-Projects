"""
File: encrypt.py
Programmer: Sharyl Hammer
Date: October 12, 2017


Encrypts a line of text. Using the Caesar Cipher.
The user inputs the line of text. The user inputs the distance value. The distance
value is the count between the character. For example the letter a would be abcdef
would be f if the distance is 5.

1. input values:
     plain text values
     the distance value

     
2. output value:
     encrypted text

"""

plainText = input("Enter a statement: ")
distance = int(input("Enter the distance value:"))

code = ""
for ch in plainText:
    ordValue = ord(ch) # finds the ordinal positin of the character value
  #  print(ordValue)
    cipherValue = ordValue + distance # finds the cipher character by adding the distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - \
                      (ord('z') - ordValue +1)
    code += chr(cipherValue)
print(code)    
     
