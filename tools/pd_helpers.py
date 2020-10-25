import pandas as pd

def apply_counts(df: pd.DataFrame, count_col: str):
    """ Denormalise a dataframe with a 'Counts' column by
    multiplying that column by the count and dropping the 
    count_col. """
    feats = [c for c in df.columns if c != count_col]
    return pd.concat([
        pd.DataFrame([list(r[feats])] * r[count_col], columns=feats)
        for i, r in df.iterrows()
    ], ignore_index=True)