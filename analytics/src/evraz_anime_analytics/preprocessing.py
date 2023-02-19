import pandas as pd


def convert_dtypes(df: pd.DataFrame):
    """
    Convert dtypes of columns in the DataFrame.
    :param df: pandas DataFrame
    :return: pandas DataFrame
    """
    df["exhauster_id"] = df["exhauster_id"].astype("uint8")
    df["gate_valve.gas_valve_closed"] = df[
        "gate_valve.gas_valve_closed"
    ].convert_dtypes()
    df["gate_valve.gas_valve_open"] = df["gate_valve.gas_valve_open"].convert_dtypes()
    df["work.is_working"] = df["work.is_working"].convert_dtypes()
    return df


def set_time_index(df: pd.DataFrame):
    """
    Set time index of the DataFrame.
    :param df: pandas DataFrame
    :return: pandas DataFrame
    """
    df = df.set_index("created_at").sort_index()
    return df


def remove_nan_and_duplicates(df: pd.DataFrame):
    """
    Remove NaN and duplicates from the DataFrame.
    :param df: pandas DataFrame
    :return: pandas DataFrame
    """
    df = df.dropna(subset=["work.is_working"])
    df_groupby = df.groupby("exhauster_id").bfill()
    for column_id in range(len(df_groupby.columns)):
        df.loc[:, df_groupby.columns[column_id]] = df_groupby[
            df_groupby.columns[column_id]
        ]
    return df
