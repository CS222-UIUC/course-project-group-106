# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=unused-variable
# pylint: disable=duplicate-code

from pathlib import Path
import pandas as pd
from budget_tracker import tally_categories
from budget_tracker import calc_account_balance

def test_can_read_data():
    df = pd.read_csv('data/transactions.csv')
    assert df is not None

def test_account_has_money():
    assert calc_account_balance() > 0

def test_pyexists():
    my_file = Path('./Spending Pie Chart.png')
    assert my_file.is_file()

def test_category_to_spent():
    dictionary = tally_categories()
    assert dictionary is not None
