"""
Program: nautical.py
Author: Sharyl Hammer
Date: September 18, 2017

The purpose of this program is to calculate nautical miles from kilometers.
Given a kil0meter represents 1/10,000 of the distance between the North Pole and
the equator.
There are 90 degrees, containing 60 minutes of arc each, between the North Pole and
the equator. A nutical mile is 1 minute of a arc.

Calculation nmi = km * 90 *60 / 10,000

1. Significant constants
   nintety = 90
   arc = 60
   1/10,000 = .0001
   distance = .0001 

2. The inputs are
   kilometers
   
3.Computations are
   nmi = km*90*60/.0001
    
4. The outputs are
   nautical miles
 """
# Intialize the constants

ARC = 60
NINETY = 90
DISTANCE = .0001

kilometers = float(input("Enter the number of kilometers:"))

nmi = kilometers * NINETY * ARC / DISTANCE
nautical = round(nmi)

print("The nautical mile conversion is " + str(nautical) + " nmi.")
#print("The income tax is $" + str(round(incomeTax)))

