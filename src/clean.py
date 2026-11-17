"""
Load and clean the raw exoplanet data.
"""

import numpy as np
import pandas as pd

RAW_PATH = "data/raw/exoplanets.csv"

TEXT_COLS = ["pl_name", "hostname", "discoverymethod", "disc_facility", "pl_bmassprov"]
NUMERIC_COLS = ["pl_orbper", "pl_orbsmax", "pl_rade",
                "pl_radeerr1", "pl_radeerr2", "pl_bmasse", "sy_dist"]

#columns where zero or negative values are impossible
MUST_BE_POSITIVE = ["pl_orbper", "pl_orbsmax", "pl_rade", "pl_bmasse", "sy_dist"]

def load_raw(path: str = RAW_PATH) -> pd.DataFrame:
    return pd.read_csv(path)

def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    #row per planet
    df = df.drop_duplicates(subset="pl_name")

    #tidy text cols
    for col in TEXT_COLS:
        df[col] = df[col].str.strip()


    #force numeric cols to numbers
    for col in NUMERIC_COLS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    #convert to integer type which allows missing values
    df["disc_year"] = df["disc_year"].astype("Int64")

    #impossible values removed
    for col in MUST_BE_POSITIVE:
        df.loc[df[col] <= 0, col] = np.nan

    return df