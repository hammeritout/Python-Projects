tolerance = 0.000001
estimate = 1.0
result = 0
import math
data = input("Please enter a number or just enter to quit: ")


while data != " ":
       if not data:
          break
       else:
         number = float(data)
         number = math.sqrt(number)
       
         print("Python's square root: ", number)
         data = input("Please enter a number or just enter to quit: ")
       
       
      
