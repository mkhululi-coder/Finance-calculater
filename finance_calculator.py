import math

#Print instructions for the user.
print("choose either 'investment' or 'bond' from the menu below to proceed:")
#Print definitions for "investment" and bond for the user.
print("investment - to calculate the amount of the interest you'll earn on interest")
print("bond - to calculate the amount you'll have to pay on a home loan")

interest = ""

#Request user to choose either investment or bond.
financial_calculation = input("Choose either investment or bond: ").lower()
if financial_calculation == "investment":
    #Request user to enter deposit amount.
    deposit_amount = int(input("Enter deposit amount: "))
    #Request user to enter interest rate.
    interest_rate = int(input("Enter interest rate: "))
    #Request user to enter number of years of investments.
    num_years = int(input("Enter number of years: "))

    interest = input("Choose either simple or compound: ")

#If user chooses simple interest.
if interest == "simple":
    #Use the python simple interest method.
    simple_interest = deposit_amount * (1 +(interest_rate/100) * num_years)
    print(f'Your simple is: {simple_interest}')

if interest == "compound":
    #Use the python compound interest method.
    compound_interest = deposit_amount*math.pow((1+interest_rate/100), num_years)
    print(f'Your compund interest is: {compound_interest}')

    
#If user chooses bond.
if financial_calculation == "bond":
    #Request user to input present value of the house.
    present_house_value = float(input("Please input house value: "))
    #Request user to input interest rate.
    interest_rate = float(input("Please input interest rate: "))
    #Request user to input number of months for bond repayment.
    num_of_months = float(input("Please input number of months Calcution of the bond: "))
    
    #Use the python bond formula to calculate the house repayment.
    bond_repayment = ((interest_rate/100/12)*present_house_value)/(1-(1+interest_rate/100/12))**(-num_of_months)
    #Print bond house repayment.
    print(f'Bond house repaymest is: {bond_repayment}')
                      
                        
    
    




