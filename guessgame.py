"""
Program: guessgame.py
Author: Sharyl Hammer
Date: October 1, 2017

The purpose of this program is to identify a number that and the computer guesses  .
The your number. The computer must make no more than the minimum number of guesses

1. The input is
   smaller number
   larger number

2. Computations:
   uses if statements to find the number      
   """



userNumber = int(input("Enter your number:"))
smaller = int(input("Enter a smaller number than your number: "))
larger = int(input("Enter a larger number then your number:"))
guessNumber = 0
 # changed the behavior of the while loop.
 # the condition that breaks the loop is when the program guesses the number.
 

count = 0
while (userNumber != guessNumber):
    guessNumber = int(input("Enter your guess number:"))    
    count +=1
    
    if guessNumber < userNumber:
        print("Your number guess is too small")
    elif guessNumber > userNumber:
        print("Your number guess is too large")
    else:
        print("Congratulations! You've guessed the number in", count, "tries!")
        
    
                          
