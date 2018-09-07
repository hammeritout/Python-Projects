"""
File: squareroot.py
Illustrates the definition of a main function.
"""

def main():
    """ The main funciton for this script."""
import math
data = input("Please enter a number or just enter to quit: ")
while data != " ":
    if not data:
       break
    else:
         number = float(data)
         result = newton(number)
        printf("The square of the number is ", result)  
data = input("Please enter a number or just enter to quit: ")         

def newton(number):
    number = math.sqrt(number)
    return number
    
main()

