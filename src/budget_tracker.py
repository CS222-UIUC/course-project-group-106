# pylint: disable=missing-docstring
# pylint: disable=invalid-name

import pandas as pd
# import numpy as np

# Read in the data
df = pd.read_csv('data/transactions.csv')

# print out the data
print(df)

account_balance = 0
# add the 'Amount' column to amount_sum if the "Transaction Type" is "credit" 
for index, row in df.iterrows():
    if row['Transaction Type'] == 'credit':
        account_balance += row['Amount']
    if row['Transaction Type'] == 'debit':
        account_balance -= row['Amount']

print(account_balance)
