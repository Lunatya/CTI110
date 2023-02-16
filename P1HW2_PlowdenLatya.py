#This program calculates and displays travel expenses
#02-16-2023
#CTI-110 P1HW2 - Travel Expense
#Latya Plowden
print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter budget: "))
print()
location = input("Enter your travel destination: ")
print()
fuel = float(input("How much do you think you will spend on gas? "))
print()
hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))
print()
print("------------ Travel Expenses ------------")
print("Location: ",location)
print("Initial Budget: ",budget)
print()
print("Fuel: ",fuel)
print("Accomodation: ",hotel)
print("Food: ",food)
print()
balance = budget - fuel - food - hotel
print("Remaining Balance: ",balance)



