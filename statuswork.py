"""
File: statuswork.py
Illustrates the definition of a main function.
"""


def main():
    """ The main funciton for this script."""
    user_input = input("Please enter five numbers separated by a single space only: ")
    input_numbers = [int(i) for i in user_input.split(' ') if i.isdigit()]
    result = mean(input_numbers)

    print("The mean is ", result)  

   # list = (input("Enter a number list:")

   # result = mean(list)
    

def mean(input_numbers):
   
    sum = 0
    for number in input_numbers:
        sum +=  number
        
    return sum/len(input_numbers)
# The entry point for program execution."""

main()
