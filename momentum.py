"""
Program: momentum.py
Author: Sharyl Hammer
Date: September 18, 2017

The purpose of this program is to calculate momentum and kinetic energy.
An object's momentum is calculated by the mass x velocity.

1. Inputs are
   mass in kilograms
   

2. Computations are
   momentum = mass x velocity
   kinetic_energy = 0.5 x mass x velocity2  
   

3. The outputs are
   momomentum
   kinetic_energy 
   
"""


mass = float(input("Enter the mass in kilograms:"))
velocity = float(input("Enter the velocity in m/s:"))


momentum = mass * velocity
mom = round(momentum,2)
kinetic_energy = 0.5 * mass * velocity ** 2
kinetic = round(kinetic_energy,2)


print("Your momentum is " + str(mom) + " kg-m/s.")
print("Your kinetic energy is " + str(kinetic) + " joules.")


