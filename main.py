import numpy as np
import pandas as pd
from datetime import date


GOODS_OR_SERVICES = []
PRICES = []
DATES = []
EXPENSE_TYPES = []

#create a function to add the expenses to the lists and organize the data
def add_expenses(goods_or_services, price, date, expense_type):
    GOODS_OR_SERVICES.append(goods_or_services)
    PRICES.append(price)
    DATES.append(date)
    EXPENSE_TYPES.append(expense_type)

#main program
#create an option menu with the options to choose from
while True:
    print("Welcome to the Expense Tracker")
    print("What would you like to do today?")
    print("1. Add food expenses")
    print("2. Add household expenses")
    print("3. Add transportation expenses")
    print("4. View and save expenses")
    print("0. Exit")   
    option = int(input("Choose an option: "))    

#print a new line
    print()

#check for the users option or input
    if option == 0: 
      print("Goodbye")
      break 
    elif option == 1:
      print("Add food expenses")
      expense_type = 'food'
    elif option == 2:   
      print("Add household expenses")
      expense_type = 'household'
    elif option == 3:
      print("Add transportation expenses")
      expense_type = 'transportation'
    elif option == 4:
      #create a dataframe and add the expenses
      expense_record = pd.DataFrame()
      expense_record['GOODS_OR_SERVICES'] = GOODS_OR_SERVICES
      expense_record['PRICES'] = PRICES
      expense_record['DATES'] = DATES
      expense_record['EXPENSE_TYPES'] = EXPENSE_TYPES
      #save the expenses
      expense_record.to_csv('expenses.csv')
      #show the expense report
      print(expense_record)
    else:
        print("Invalid option")    
    
      


    #allow the user to enter the good or service and the price
    if option == 1 or option == 2 or option == 3:
      good_or_service = input("Enter the good or service + 'expense_type':\n ")
      price = float(input("Enter the price:\n "))
      date = date.today()
      add_expenses(good_or_service, price, date, expense_type)

    #print a new line
    print()

       
