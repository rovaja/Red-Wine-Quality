"""Helper module for EDA notebook to perform 
data cleaning and preprocessing"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import Optional, Any


def check_null_values(df: pd.DataFrame) -> Optional[pd.DataFrame]:
    """Checks for null values of the given dataset"""
    if df.empty:
        print("Dataframe is empty")
    else:
        total_amount: int = pd.isnull(df).sum().sum()
        print(f"Total number of null values in data: {total_amount}")
        if total_amount > 0:
            columns_with_nan = df.columns[df.isnull().any()].tolist()
            print(
                f"Number of null values per column:\n{pd.isnull(df[columns_with_nan]).sum()}"
            )
            return df[df.isnull().any(axis=1)]


def check_duplicated_rows(df) -> None:
    """Checks for duplicated rows of the given dataset"""
    if df.empty:
        print("Dataframe is empty")
    else:
        total_amount: int = df.duplicated().sum()
        if total_amount > 0:
            print(df[df.duplicated() == True])
        print(f"Total number of duplicated rows in data: {total_amount}")
