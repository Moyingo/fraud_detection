import os

import pandas as pd
import sweetviz as sv

from .eda_config import PATH_DATA, PATH_REPORT


def load_data():
    df = pd.read_pickle(PATH_DATA)
    return df

def create_eda(df: pd.DataFrame):
    # analyzing the dataset
    report = sv.analyze(df)
    # Check path
    if not os.path.exists(os.path.dirname(PATH_REPORT)):
        os.makedirs(os.path.dirname(PATH_REPORT))
    # display the report
    report.show_html(PATH_REPORT, open_browser=False)