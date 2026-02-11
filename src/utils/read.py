# functions to read data into pandas dataframes

import pandas as pd
import json

def json_to_df(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    return df