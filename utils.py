import pandas as pd

def load_data(file_path, index_col=None):
    """
    Load a CSV file into a pandas DataFrame.

    Parameters:
        file_path (str): Path to the CSV file.
        index_col (int, optional): Column to use as the index.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    return pd.read_csv(file_path, index_col=index_col)

def save_score(score, file_path):
    """
    Save the model score to a text file.

    Parameters:
        score (float): Model score (R²).
        file_path (str): Output text file.
    """
    with open(file_path, "w") as f:
        f.write(f"{score:.4f}")

def save_predictions(df, file_path):
    """
    Save predictions to a CSV file.

    Parameters:
        df (pd.DataFrame): DataFrame containing predictions.
        file_path (str): Output CSV file.
    """
    df.to_csv(file_path)

import joblib

def save_model(model, file_path):
    joblib.dump(model, file_path)

def load_model(file_path):
    return joblib.load(file_path)