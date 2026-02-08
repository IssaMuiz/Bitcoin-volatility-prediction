"""
Docstring for data_preprocessing.features_engineering
"""
import pandas as pd
import numpy as np


def log_return(df: pd.DataFrame):
    """
    Calculate the log return of the 'Close' price in the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing a 'Close' column.

    Returns:
    pd.DataFrame: The DataFrame with an additional 'Log_Return' column containing the log returns.
    """
    try:
        df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))
        print("Log return calculation successful.")
        return df
    except KeyError:
        print("Error: 'Close' column not found in the DataFrame.")
        raise
    except Exception as e:
        print(f"An error occurred during log return calculation: {e}")
        raise


def volatility(df: pd.DataFrame, window: int = 30):
    """
    Calculate the rolling volatility of the 'Log_Return' in the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing a 'Log_Return' column.
    window (int): The rolling window size for volatility calculation. Default is 30.

    Returns:
    pd.DataFrame: The DataFrame with an additional 'Volatility' column containing the rolling volatility.
    """
    try:
        df['Volatility'] = df['Log_Return'].rolling(
            window=window).std() * np.sqrt(window)
        print("Volatility calculation successful.")
        return df
    except KeyError:
        print("Error: 'Log_Return' column not found in the DataFrame.")
        raise
    except Exception as e:
        print(f"An error occurred during volatility calculation: {e}")
        raise


def range_of_motion(df: pd.DataFrame):
    """
    Calculate the range of motion for the 'High' and 'Low' prices in the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing 'High' and 'Low' columns.

    Returns:
    pd.DataFrame: The DataFrame with an additional 'Range_of_Motion' column containing the range of motion.
    """
    try:
        df['Range_of_Motion'] = df['High'] - df['Low']
        print("Range of motion calculation successful.")
        return df
    except KeyError:
        print("Error: 'High' or 'Low' column not found in the DataFrame.")
        raise
    except Exception as e:
        print(f"An error occurred during range of motion calculation: {e}")
        raise
