"""
Program: wage.py
Author: Sharyl Hammer
Date: September 11, 2017

The purpose of this program is to calculate an employee's total weekly pay.
This program takes inputs for the hourly wage, total regular hours and total
overtime hours.

1. Significant constants
   overtime rate

2. The inputs are
   hourly wage
   total regular hours
   total overtime hours

3. Computations:

   overtime pay = total overtime hours * overtime rate
   total weekly pay = hourly wage * regular hours + overtime pay

4. The outputs are
   total weekly pay
"""
OVERTIME_RATE = 1.5

hourlyWage=float(input("Enter your hourly wage: "))
regHours = float(input("Enter your total regular hours: "))
overtimeHours = float(input("Enter your total overtime hours: "))

wageovertimeRate = hourlyWage * OVERTIME_RATE
overtimePay = wageovertimeRate * overtimeHours
weeklyPay = hourlyWage * regHours + overtimePay

print("Your total weekly pay is $" + str(float(weeklyPay)))


   
   
