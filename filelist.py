"""
Filename: filelist.py
"""
fileName = input("Enter the filename: ")
input_list =  fileName.split(' ')
#print(input_list)

# file name needs to be placed in a list

for i, line in enumerate(input_list):
    print(i, line)

# Prints the line number with line.

line_number = input("Enter a line number or 0 to quit: " )        

for line in input_list:
   # if (line_number == input_list.index(line)):
       # this code above does not work. Not sure if I can compare here.
    # this code does print the index    
    print(input_list.index(line))
    print(line_number)

for i, line in enumerate(input_list):
        if(line_number is i,line):
            print("This is the line of the line number ", line)

            # this comparison does not work.
            # Can't find the matching line_number with the list index.
            # these statements work without the if condition. 
            #print("This is the line number" , line_number)
            
   

        
  
   




    
