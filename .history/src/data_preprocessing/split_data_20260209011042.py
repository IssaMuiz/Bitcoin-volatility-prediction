"""
Docstring for data_preprocessing.split_data
"""
from sklearn.model_selection import train_test_split
import pandas as pd


def split_data(df: pd.DataFrame):
    """
    Docstring for split_data

    :param df: Description
    :type df: pd.DataFrame
    """
    train, test = train_test_split(df, test_size=0.3, random_state=42)
    return train, test
