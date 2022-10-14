# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=duplicate-code
# pylint: disable=unused-variable


import pandas as pd
from matplotlib import pyplot as plt

# import numpy as np

# Read in the data
df = pd.read_csv('data/transactions.csv')

# print out the data
print(df)

# add the 'Amount' column to amount_sum if the "Transaction Type" is "credit"
def calc_account_balance():
    account_balance = 0
    for index, row in df.iterrows():
        if row['Transaction Type'] == 'credit':
            account_balance += row['Amount']
        if row['Transaction Type'] == 'debit':
            account_balance -= row['Amount']
    return account_balance

def unique_categories():
    return df['Category'].unique()

def tally_categories():
    tally = {}
    for index, row in df.iterrows():
        if row['Category'] in tally:
            #category already exists
            if row['Transaction Type'] == 'credit':
                #credit
                tally[row['Category']] += row['Amount']
            else:
                #debit
                tally[row['Category']] -= row['Amount']
        else:
            #create new category
            tally[row['Category']] = row['Amount']
    del tally['Transfer']
    return tally

def plot_histogram():
    x = []
    y = []
    for key, value in tally_categories().items():
        x.append(key)
        y.append(value)
    fig = plt.figure(figsize = (20, 10))
    plt.bar(x, y, color ='maroon', width = 1.0)
    plt.xticks(rotation=30, ha='right')
    
    plt.xlabel("Categories")
    plt.ylabel("Amount spent")
    plt.title("Amount spent on each category")
    plt.savefig("Amount Spent.png")

# print out the account balance
print(calc_account_balance())

plot_histogram()

def calc_food_spending():
    tally = tally_categories()
    food_spending = 0
    keys = tally.keys()
    for key in keys:
        if key == 'Restaurants' or key == 'Groceries' or key == 'Food & Dining':
            food_spending += tally.get(key)
        if key == 'Food Delivery' or key == 'Fast Food' or key == 'Coffee Shops':
            food_spending += tally.get(key)
    return food_spending


def calc_housing_spending():
    tally = tally_categories()
    housing_spending = 0
    keys = tally.keys()
    for key in keys:
        if key == 'Mortgage & Rent':
            housing_spending += tally.get(key)
    return housing_spending

def calc_transportationtravel_spending():
    tally = tally_categories()
    transportation_spending = 0
    keys = tally.keys()
    for key in keys:
        if key == 'Ride Share' or key == 'Travel' or key == 'Gas & Fuel':
            transportation_spending += tally.get(key)
        if key == 'Parking' or key == 'Air Travel' or key == 'Rental Car & Taxi':
            transportation_spending += tally.get(key)
        if key == 'Hotel':
            transportation_spending += tally.get(key)
    return transportation_spending

def calc_medical_spending():
    tally = tally_categories()
    med_spending = 0

    keys = tally.keys()
    for key in keys:
        if key == 'Dentist' or key == 'Doctor' or key == 'Pharmacy':
            med_spending += tally.get(key)
    return med_spending


def calc_utilities_spending():
    tally = tally_categories()
    utilities = 0
    keys = tally.keys()
    for key in keys:
        if key == 'Mobile Phone' or key == 'Utilities' or key == 'Gym':
            utilities += tally.get(key)
    return utilities

def calc_entertainment_spending():
    tally = tally_categories()
    entertainment = 0
    keys = tally.keys()
    for key in keys:
        if key == 'Movies & DVDs' or key == 'Music' or key == 'Entertainment' or key == 'Sporting Goods':
            entertainment += tally.get(key)
    return entertainment

def calc_school_spending():
    tally = tally_categories()
    school_spending = 0
    keys = tally.keys()
    for key in keys:
        if key == 'Books & Supplies' or key == 'Tuition':
            school_spending += tally.get(key)
    return school_spending

def calc_shopping_spending():
    tally = tally_categories()
    shopping = 0
    keys = tally.keys()
    for key in keys:
        if key == 'Shopping' or key == 'Electronics & Software' or key == 'Gift' or key == 'Clothing':
            shopping += tally.get(key)
    return shopping

def calc_misc_spending():
    tally = tally_categories()
    miscellaneous = 0
    keys = tally.keys()
    for key in keys:
        if key == 'Fees & Charges' or key == 'Uncategoried' or key == 'Charity':
            miscellaneous += tally.get(key)
        if key == 'Federal Tax' or key == 'Misc Expenses' or key == 'Bank Fee':
            miscellaneous += tally.get(key)
        if key == 'Business Services':
            miscellaneous += tally.get(key)
    return miscellaneous

# entertainment, school, shopping, miscellaneous

tally_categories()
