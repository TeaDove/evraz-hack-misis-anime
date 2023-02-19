from datetime import datetime, timedelta
from typing import List, Tuple

import numpy as np
import pandas as pd

from .preprocessing import convert_dtypes, remove_nan_and_duplicates, set_time_index

WARNING_PENALTY_LEN_COEF = 0.05
WARNING_PENALTY_DIFF_COEF = 0.25
ALARM_PENALTY_LEN_COEF = 0.3
ALARM_PENALTY_DIFF_COEF = 2.275

FREQ = "15min"
MAX_REPAIR_DURATION = 20


def load_data(path: str) -> pd.DataFrame:
    """Load data from path and return it as a pandas DataFrame.

    :param path: path to the data
    :return: pandas DataFrame
    """
    return pd.read_parquet(path)


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocess data and return it as a pandas DataFrame.

    :param df: pandas DataFrame
    :return: pandas DataFrame
    """
    df = convert_dtypes(df)
    df = set_time_index(df)
    df = remove_nan_and_duplicates(df)
    return df


def get_data_from_exhauster_by_id(df: pd.DataFrame, exhauster_id: int) -> pd.DataFrame:
    """Get data from exhauster by id and return it as a pandas DataFrame.

    :param df: pandas DataFrame
    :param exhauster_id: exhauster id
    :return: pandas DataFrame
    """
    exdf = df[df["exhauster_id"] == exhauster_id]
    return exdf


def resample_data(df: pd.DataFrame, freq: str = "1min") -> pd.DataFrame:
    """Resample data and return it as a pandas DataFrame.

    :param df: pandas DataFrame
    :param freq: resampling frequency
    :return: pandas DataFrame
    """
    df_resampled = df.resample(freq).mean(numeric_only=True)
    # df_resampled = remove_nan_and_duplicates(df_resampled)
    return df_resampled


def get_regions(x: np.ndarray) -> List[List[int]]:  # noqa: CCR001
    """
    Get regions of the DataFrame.
    :param df: pandas DataFrame
    :return: list of regions
    """
    regions: List[List[int]] = []
    region_continous = False
    for i, k in enumerate(x):
        if k:
            if not region_continous:
                regions.append([i])
                region_continous = True
            else:
                if regions:
                    regions[-1].append(i)
        else:
            region_continous = False
    return regions


def get_data_from_last_repairment(df: pd.DataFrame, last_repairment_date: datetime) -> pd.DataFrame:
    """
    Get data from last repairment of the DataFrame.
    :param df: pandas DataFrame
    :param exhaust_id: exhauster id
    :param last_repairment_dates: list of last repairment dates
    :return: pandas DataFrame
    """
    df = df[df.index >= last_repairment_date]
    return df


def find_closest_business_day(date: datetime) -> datetime:
    """
    Find closest business day.
    :param date: datetime
    :return: datetime
    """
    if date.weekday() == 5:
        date = date + timedelta(days=2)
    elif date.weekday() == 6:
        date = date + timedelta(days=1)
    return date


def find_out_of_norm_samples(
    df: pd.DataFrame,
) -> Tuple[List[List[int]], List[List[float]], List[List[int]], List[List[float]],]:  # noqa: TAE002
    """Find out of norm samples in the DataFrame.
    :param df: pandas DataFrame
    :return: list of out of norm samples
    """
    out_of_norm_points_warning_all = []
    warning_diffs_all = []
    out_of_norm_points_alarm_all = []
    alarm_diffs_all = []
    for bearing_id in range(1, 10):
        for k in [
            "temperature",
            "vibration.vibration_axial",
            "vibration.vibration_horizontal",
            "vibration.vibration_vertical",
        ]:
            sel_col = f"bearing_{bearing_id}.{k}.value"
            if sel_col in df.columns:
                out_of_norm_points_warning = (df[sel_col] > df[f"bearing_{bearing_id}.{k}.warning_max"]).to_numpy()
                df_ow = df[out_of_norm_points_warning]
                diff_warning = df_ow[sel_col] - df_ow[f"bearing_{bearing_id}.{k}.warning_max"]
                out_of_norm_points_alarm = (df[sel_col] > df[f"bearing_{bearing_id}.{k}.alarm_max"]).to_numpy()
                df_oa = df[out_of_norm_points_alarm]
                diff_alarm = df_oa[sel_col] - df_oa[f"bearing_{bearing_id}.{k}.alarm_max"]

                out_of_norm_points_warning_regions = get_regions(out_of_norm_points_warning)
                out_of_norm_points_alarm_regions = get_regions(out_of_norm_points_alarm)

                out_of_norm_points_warning_all.extend(out_of_norm_points_warning_regions)
                out_of_norm_points_alarm_all.extend(out_of_norm_points_alarm_regions)

                warning_diffs_all.extend(diff_warning)
                alarm_diffs_all.extend(diff_alarm)
    return (
        out_of_norm_points_warning_all,
        warning_diffs_all,
        out_of_norm_points_alarm_all,
        alarm_diffs_all,
    )


def calculate_penalty(  # noqa: CCR001
    warning_regions: List[List[int]],
    warning_diffs: List[List[float]],
    alarm_regions: List[List[int]],
    alarm_diffs: List[List[float]],
) -> timedelta:
    """Calculate penalty for the DataFrame.
    :param df: pandas DataFrame
    :param warning_regions: list of warning regions
    :param alarm_regions: list of alarm regions
    :return: penalty
    """
    penalty: float = 0.0
    for region, diff in zip(warning_regions, warning_diffs):
        if region is not None and diff is not None:
            penalty += (
                np.mean(diff) * WARNING_PENALTY_DIFF_COEF + len(region) * WARNING_PENALTY_LEN_COEF
            )  # type: ignore
    for region, diff in zip(alarm_regions, alarm_diffs):
        if region is not None and diff is not None:
            penalty += np.mean(diff) * ALARM_PENALTY_DIFF_COEF + len(region) * ALARM_PENALTY_LEN_COEF  # type: ignore
    return timedelta(hours=penalty)
