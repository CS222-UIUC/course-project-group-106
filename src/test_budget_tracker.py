# pylint: disable=missing-docstring
# pylint: disable=invalid-name
import pandas as pd

def test_can_read_data():
    df = pd.read_csv('data/transactions.csv')
    assert df is not None

def test_account_has_money():
    df = pd.read_csv('data/transactions.csv')
    account_balance = 0
    for index, row in df.iterrows():
        if row['Transaction Type'] == 'credit':
            account_balance += row['Amount']
        if row['Transaction Type'] == 'debit':
            account_balance -= row['Amount']
    assert account_balance > 0