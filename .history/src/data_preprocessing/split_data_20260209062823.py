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
    try:

        train_val_df,  test_df = train_test_split(
            df, test_size=0.2, random_state=42)

        train_df, val_df = train_test_split(
            train_val_df, test_size=0.25, random_state=42)
        print("Data splitted successfully!")
        return train_df, val_df, test_df

    except Exception as e:
        print(f"An error occured while splitting the dataset: {e}")
        raise
