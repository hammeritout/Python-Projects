
"""
File: status.py
Illustrates the definition of a main function.
"""

def main():
    """ The main funciton for this script."""

    user_input = input("Please enter numbers separated by a single space only: ")
    input_numbers = [int(i) for i in user_input.split(' ') if i.isdigit()]
    # calls the method mean and passes the input_numbers in a param and passes
    # back the calculated mean number. 
    sum = mean(input_numbers)
    list = mode(input_numbers)

    print("The mean is ", sum)  
    print("The mode is ", list)
     

def mean(input_numbers):
   
    sum = 0
    for number in input_numbers:
        sum +=  number
        
    return sum/len(input_numbers)

def mode(input_numbers):
    
    # first sort the number list.
    input_numbers.sort()
    theDictionary = {}
    for number in input_numbers:
        result = theDictionary.get(number,None)
        if result == None:
            # the number is entered the first time
            theDictionary[number] = 1
        else:
            # the number is  found more than once placed in theDictionary 
            theDictionary[number] = number + 1

    # mode is calculated and passed in the return statement   
    theMaximum = max(theDictionary.values())
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
           break 
          

    return key      
        
    

main()

