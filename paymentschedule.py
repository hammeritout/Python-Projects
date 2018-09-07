"""
Program: paymentschedule.py
Author: Sharyl Hammer

Computes a Payment Schedule.

1. The inputs are:
       purchase price

2. The report is displayed in tabular form with a header.

3. Computations:

  1. balance owed
     balance owed = purchase price * DOWN_PAY
     starting balance - princpal = newbalance
  2  principal = payment - interest
     payment = starting balance * .05 
     starting balance = purchase price - downPay
      900 = 1,000 * .10
    
   3. interest 
      interest = starting balance - INTERST_RATE /12   
   4. constants:

   INTEREST_RATE = 0.12
   DOWN_PAY = 0.10
   MONTH_RATE = 0.05

         """

#Initialize the constants
INTEREST_RATE = 0.12
DOWN_PAY = 0.10
MONTH_RATE = 0.05

purchasePrice = float(input("Enter the purchase price: "))
month = 1

subpay = purchasePrice * DOWN_PAY
balanceOwed = purchasePrice - subpay
startBalance = purchasePrice - subpay

print("%5s%14s%10s%11s%9s%9s" % \
     ("Month", "Balance Owed", "Interest", "Principal", "Payment", "Balance"))
##print("\n")

while balanceOwed != 0:
##while month <= 23:
      
      monthInterest = balanceOwed * INTEREST_RATE / 12
      monthPayment = startBalance * MONTH_RATE
      principal = monthPayment - monthInterest
      monthlyBalance = balanceOwed - principal
      if monthlyBalance > 0:
         balanceOwed = monthlyBalance
      else:
         monthPayment = balanceOwed + monthInterest       
         principal = monthPayment - monthInterest
         monthlyBalance = 0 
         balanceOwed = monthlyBalance

      print("%4d%14.2f%10.2f%11.2f%9.2f%9.2f" % \
           (month,balanceOwed,monthInterest,principal,monthPayment,monthlyBalance))  
     # tested program variables here. 
     # print("The month is", month)   
    #  print("The balance owed is $%0.2f" % balanceOwed)
     # print("The monthly interest is $%0.2f" % monthInterest)
     # print("The monthly payment is $%0.2f" % monthPayment)
    #  print("The principal is $%0.2f" % principal)
    #  print("The monthly balance is $%0.2f" % monthlyBalance)
    #  print("\n")
      #balancedOwed = monthlyBalance - #got in a loop here
      # program is designed that the control of the loop is the balanceOwed which
      
      month +=1
      


    




