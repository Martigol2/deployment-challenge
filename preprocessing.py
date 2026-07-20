def drop_unnamed_column(df):
    """
    Remove the automatically generated index column if it exists.
    """
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    return df


def filter_open_stores(df):
    """
    Keep only rows where the store is open.

    Parameters:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame containing only open stores.
    """
    return df[df["open"] == 1]

def drop_open_column(df):
    """
    Remove the 'open' column from the DataFrame.

    Parameters:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame without the 'open' column.
    """
    if "open" in df.columns:
        df = df.drop(columns=["open"])

    return df

def drop_date_column(df):
    """
    Remove the 'date' column from the DataFrame.

    Parameters:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame without the 'date' column.
    """
    if "date" in df.columns:
        df = df.drop(columns=["date"])

    return df

def encode_state_holiday(df):
    """
    Encode the 'state_holiday' column as a binary variable.

    0 -> 0 (not a holiday)
    a, b, c -> 1 (holiday)

    Parameters:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with the encoded 'state_holiday' column.
    """
    if "state_holiday" in df.columns:
        df["state_holiday"] = df["state_holiday"].apply(
            lambda x: 0 if x == "0" else 1
        )

    return df

def drop_duplicates(df):
    """
    Remove duplicate rows from the DataFrame.

    Parameters:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame without duplicate rows.
    """
    return df.drop_duplicates()