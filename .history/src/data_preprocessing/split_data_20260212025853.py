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
        n = len(df)
        train_end = (n * 0.7)
        val_end = (n * 0.85)

        train_df = df.iloc[:train_end]
        val_df = df.iloc[train_end:val_end]
        test_df = df.iloc[val_end:]

        print("Data splitted successfully!")
        return train_df, val_df, test_df

    except Exception as e:
        print(f"An error occured while splitting the dataset: {e}")
        raise


def split_features(df: pd.DataFrame):
    """
    Docstring for splitting features
    """

    try:
        X = df.drop(columns=['Target_Volatility',
                    'Volatility', 'Start', 'End'])
        y = df['Target_Volatility']
        print("Features splitted into target and dependent features ")
        return X, y

    except Exception as e:
        print(f"An error occured while splitting features: {e}")
        raise
