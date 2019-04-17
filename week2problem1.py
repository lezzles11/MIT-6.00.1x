"""
Paying Debt off in a year
Goal: Calculate credit card balance after one year if a person only pays min
monthly payment required by credit card

balance: outstanding balance
annualInterestRate: annual interest rate as a decimal
monthlyPaymentRate: minimum monthly payment (decimal)

For each month, calculate statements on monthly payment and remaining balance.
At the end of 12 months, print out remaining balance.

Make sure two decimals. 
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)


#Month... 
month = 0
#Remaining balance
remaining = 0

#person will type in current balance 
balance = input("Balance = ")

annualInterestRate = input("annualInterestRate = ")
monthlyInterest = annualInterestRate / 12.0

minRate = (input"monthlyPaymentRate = ")
minMonthlyPayment = minRate x balance

unpaid = balance - (minRate x balance)


balance - 

updated = balance - (minRate * balance) + (monthlyInterest * balance - (minRate x balance))

while month <= 12:
    remaining = balance - minMonthlyPayment
    balance = 
    
    month = month + 1
"""

"""
DEFINITELY RIGHT:
balance = 42
monthlyInterest = 0.2 / 12
minMonthlyPayment = 0.04 * balance
unpaid = balance - minMonthlyPayment
notTaxed = balance - minMonthlyPayment
taxed = monthlyInterest * notTaxed
remaining = unpaid + taxed
print(remaining)
remaining = balance
"""


#print out what your balance would be after one month

month = 0
balance = input("Balance: ")
monthlyInterest = float(0.2 / 12)

while month <= 11:
    minMonthlyPayment = float(0.04) * float(balance)
    unpaid = float(balance) - float(minMonthlyPayment)
    notTaxed = float(balance) - float(minMonthlyPayment)
    taxed = float(monthlyInterest) * float(notTaxed)
    remaining = float(unpaid) + float(taxed)
    print(round(remaining, 2))
    balance = float(remaining)
    month = int(month) + 1
    





    
