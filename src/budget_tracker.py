# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=duplicate-code
# pylint: disable=unused-variable

import pandas as pd
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
            tally[row['Category']] += row['Amount']
        else:
            tally[row['Category']] = row['Amount']
    return tally

# print out the account balance
print(calc_account_balance())
