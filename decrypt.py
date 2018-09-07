"""
File: decrypt.py
Programmer: Sharyl Hammer
Date: October 12, 2017


Decrpyts a line of cipher text. Using the Caesar Cipher.
The user inputs the cipher text. The user inputs the distance value. The distance
value is the count between the character. 

1. input values:
     encrpted text values
     the distance value

     
2. output value:
      plain text value

"""
code = input("Enter the cipher text: ")
distance = int(input("Enter the distance value: "))
plainText = " "

for ch in code:
   # print(ch)
    ordValue = ord(ch)
    cipherValue = ordValue - distance # going other direction. right to left
      # by passes capital characters
    if ch.islower() and cipherValue < ord('a'): 
   
       cipherValue = ord('z') - \
                     (distance + (ord('a')- (ordValue + 1 )))
       # found with these tests that the distance needed to be + insteatd of -.
       # When you had a negative number with the subtraction it would add and get the
       # wrong value. The book uses the wrong calculation.
       # Changed program to handles capitalization.
      # print("This is the ordValue", ordValue + 1)
      # test = (ord('a') - (ordValue + 1))
      # distest = (distance + test)
      # print ("This is the calculation of distance ", distest) 
     #  print("This is the value of test " , test)
     #  print(cipherValue)  
    plainText += chr(cipherValue)
print(plainText)

