import pandas as pd

from .preprocessing_config import COLUMNS_TO_NUMERIC


def transform_to_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """
    The transform_to_numeric function takes a dataframe as input and returns the same dataframe with
    the columns specified in COLUMNS_TO_NUMERIC transformed to numeric values.


    :param df: pd.DataFrame: Specify the type of dataframe that is being passed in
    :return: A dataframe with the columns in columns_to_numeric
    :doc-author: Ricardo Moya
    """
    for col in COLUMNS_TO_NUMERIC:
        df[col] = df[col].astype(float)
    return df
