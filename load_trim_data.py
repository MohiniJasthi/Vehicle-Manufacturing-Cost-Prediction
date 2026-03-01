
import os
import glob
import pandas as pd

def load_trim_table(parts_dir: str) -> pd.DataFrame:
    """
    Load all Trim_table_part*.csv from a directory and return one DataFrame.
    """
    pattern = os.path.join(parts_dir, "Trim_table_part*.csv")
    files = sorted(glob.glob(pattern))
    if not files:
        raise FileNotFoundError(f"No trim parts found with pattern: {pattern}")
    dfs = [pd.read_csv(f) for f in files]
    return pd.concat(dfs, ignore_index=True)
