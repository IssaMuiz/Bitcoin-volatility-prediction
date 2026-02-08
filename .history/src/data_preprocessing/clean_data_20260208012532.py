"""Data cleaning module for Bitcoin price data preprocessing"""
import pandas as pd


def datetime_conversion(df, column):
    """
    Convert the 'Start' column in the DataFrame to datetime format.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing a 'Start' column.

    Returns:
    pd.DataFrame: The DataFrame with the 'Start' column converted to datetime format.
    """
    try:
        df[column] = pd.to_datetime(df[column])
        df = df.sort_values(by=column)
        df = df.set_index(column, inplace=True)
        print(f"DateTime conversion successful for column '{column}'.")
        return df
    except KeyError:
        print(f"Error: Column '{column}' not found in the DataFrame.")
        raise
    except Exception as e:
        print(f"An error occurred during DateTime conversion: {e}")
        raise


def drop_na(df):
    """
    Drop rows with missing values from the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    pd.DataFrame: The DataFrame with rows containing missing values dropped.
    """
    initial_shape = df.shape
    df = df.dropna().reset_index(drop=True)
    final_shape = df.shape
    print(
        f"Dropped {initial_shape[0] - final_shape[0]} rows with missing values.")
    return df
