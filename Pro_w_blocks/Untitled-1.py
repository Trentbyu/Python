"""
File: meal_price_calculator.py
Author: Minto N. Brown
Purpose: 03 Prove: Milestone - Meal Price Calculator
"""
# User input
print()
cost_of_meal_child = float(input('What is the price of a child\'s meal? '))
cost_of_meal_adult = float(input('What is the price of an adult\'s meal? '))
cost_of_drink = float(input('What is the price of a drink? '))
number_of_child = int(input('How many children are there? '))
number_of_adult = int(input('How many adults are there? '))
number_of_drink = int(input('How many drinks were ordered? '))
tax = float(input('What is the sales tax rate? '))
print()
# Cost calculation, place holder
subtotal = (cost_of_meal_child * number_of_child) + (cost_of_meal_adult * 
number_of_adult) +  (cost_of_drink * number_of_drink) 
sales_tax = subtotal * tax * 0.01
total = subtotal + sales_tax
# Cost output
print(f'Subtotal: ${subtotal}')
print(f'Sales Tax: ${sales_tax}')
print(f'Total: ${total}\n')
#Payment and tip input
payment = float(input('What is the payment amount? '))
tip = float(input('How much would you like to tip? '))
# Change calculation
change = payment - (total + tip)
# Change output
if (total + tip) > payment:
    print('Not enough payment')
else:
    print(f'Change: ${change}')