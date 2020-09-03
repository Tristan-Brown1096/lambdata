"""Unit tests for the objects and functions of the lambdata package"""


import unittest
from functions import MyDataFrame
from example_module import TEST
import pandas as pd

DATA_PATH = 'https://raw.githubusercontent.com/LambdaSchool/DS-Unit-2-Kaggle-Challenge/master/data/'


class FunctionsTest(unittest.TestCase):
    """Making sure the object functions properly"""
    def setUp(self):
        self.df = MyDataFrame
        (pd.read_csv(DATA_PATH+'waterpumps/train_features.csv'
                     parse_dates=['date_recorded']))

    def test_mydataframe(self):
        """Tests that the dataframe imports properly"""
        df = MyDataFrame(pd.DataFrame(TEST))
        self.assertTrue(df[0][0], pd.DataFrame(TEST)[0][0])

    def test_wrangle(self):
        df = self.df.wrangle()
        self.assertEqual(df.shape, (14358, 32))

    def test_datesplit(self):
        df = self.df.date_split()
        self.assertEqual(df['date_recorded_year'][0], 2013)


if __name__ == '__main__':
    unittest.main()
