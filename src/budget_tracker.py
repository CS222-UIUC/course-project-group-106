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