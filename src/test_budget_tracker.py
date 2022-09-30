# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=unused-variable
# pylint: disable=duplicate-code

import pandas as pd
from budget_tracker import calc_account_balance

def test_can_read_data():
    df = pd.read_csv('data/transactions.csv')
    assert df is not None

def test_account_has_money():
    assert calc_account_balance() > 0
