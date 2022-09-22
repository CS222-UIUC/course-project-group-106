# pylint: disable=missing-docstring
# pylint: disable=invalid-name
import pandas as pd

def test_can_read_data():
    df = pd.read_csv('data/transactions.csv')
    assert df is not None
