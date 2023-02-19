from datetime import datetime, timedelta
from typing import List, Optional, Tuple

import pandas as pd
from evraz_anime_analytics.helper import (
    FREQ,
    MAX_REPAIR_DURATION,
    calculate_penalty,
    find_closest_business_day,
    find_out_of_norm_samples,
    get_data_from_exhauster_by_id,
    get_data_from_last_repairment,
    resample_data,
)


def predict(
    df: pd.DataFrame,
    last_repairment_dates: Optional[List[datetime]] = None,
    freq=FREQ,
    max_repairment_duration=MAX_REPAIR_DURATION,
) -> List[Tuple[int, datetime]]:
    """
    Predict the next repairment date.
    :param df: pandas DataFrame
    :param last_repairment_dates: list of last repairment dates
    (if not provided, last_repairment_date column must be provided in df)
    :param freq: resampling frequency
    :param max_repairment_duration: maximal amount of days between repairments
    :return: list of tuples (exhauster_id, next_repairment_date)
    """
    if last_repairment_dates is None and "last_repairment_date" not in df.columns:
        raise ValueError("last_repairment_dates or last_repairment_date column must be provided")
    if last_repairment_dates is None:
        last_repairment_dates = [  # noqa: ECE001
            df[df["exhauster_id"] == i]["last_repairment_date"].iloc[0] for i in range(6)
        ]

    exdf = [resample_data(get_data_from_exhauster_by_id(df, i), freq=freq) for i in range(6)]
    exdf_shortened = [get_data_from_last_repairment(exdf[i], last_repairment_dates[i]) for i in range(6)]
    days_since_last_repairment = [(datetime.now() - last_repairment_dates[i]).days for i in range(6)]
    days_before_repairment = [
        timedelta(days=max(0, max_repairment_duration - days_since_last_repairment[i])) for i in range(6)
    ]
    oonrs = [find_out_of_norm_samples(exdf_shortened[i]) for i in range(6)]
    penalties = [calculate_penalty(*oonrs[i]) for i in range(6)]
    days_before_repairment_with_penalty = [
        max(timedelta(0), days_before_repairment[i] - penalties[i]) for i in range(6)
    ]
    closest_repairment_date = [
        find_closest_business_day(datetime.now() + days_before_repairment_with_penalty[i]).date() for i in range(6)
    ]
    return list(zip(range(6), closest_repairment_date))
