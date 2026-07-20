from sklearn.model_selection import train_test_split

def split_data(df, target="sales", test_size=0.3, random_state=42):
    """
    Split the dataset into training, validation, and test sets.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        target (str): Name of the target column.
        test_size (float): Fraction of the data reserved for validation and test.
        random_state (int): Random seed for reproducibility.

    Returns:
        tuple:
            X_train, X_val, X_test,
            y_train, y_val, y_test
    """

    # Features and target
    X = df.drop(columns=[target])
    y = df[target]

    # 70% train / 30% temp
    X_train, X_temp, y_train, y_temp = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )

    # Split temp into validation and test (15% each)
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp,
        y_temp,
        test_size=0.5,
        random_state=random_state
    )

    return X_train, X_val, X_test, y_train, y_val, y_test

import numpy as np
from sklearn.metrics import mean_absolute_error, r2_score

def evaluate_baseline(y_train, y_val):
    """
    Evaluate a baseline model that always predicts the mean of the training target.

    Parameters:
        y_train (pd.Series): Training target.
        y_val (pd.Series): Validation target.

    Returns:
        tuple:
            baseline_prediction (float)
            mae (float)
            r2 (float)
    """

    # Predict the mean of the training target
    baseline_prediction = np.mean(y_train)

    # Create predictions for the validation set
    predictions = np.full(len(y_val), baseline_prediction)

    # Evaluate
    mae = mean_absolute_error(y_val, predictions)
    r2 = r2_score(y_val, predictions)

    return baseline_prediction, mae, r2

from sklearn.preprocessing import StandardScaler

def scale_feature(X_train, X_val, X_test, column):
    """
    Fit a StandardScaler on the training set and transform the
    specified column in the training, validation, and test sets.

    Parameters:
        X_train (pd.DataFrame): Training features.
        X_val (pd.DataFrame): Validation features.
        X_test (pd.DataFrame): Test features.
        column (str): Name of the column to scale.

    Returns:
        tuple:
            X_train, X_val, X_test, scaler
    """

    scaler = StandardScaler()

    # Fit only on training data
    scaler.fit(X_train[[column]])

    # Transform all datasets
    X_train[column] = scaler.transform(X_train[[column]])
    X_val[column] = scaler.transform(X_val[[column]])
    X_test[column] = scaler.transform(X_test[[column]])

    return X_train, X_val, X_test, scaler

import numpy as np
from sklearn.metrics import mean_absolute_error, r2_score

def evaluate_baseline(y_train, y_val):
    """
    Evaluate a baseline model that always predicts the mean of the training target.
    """

    baseline_prediction = np.mean(y_train)

    predictions = np.full(len(y_val), baseline_prediction)

    mae = mean_absolute_error(y_val, predictions)
    r2 = r2_score(y_val, predictions)

    return baseline_prediction, predictions, mae, r2

from sklearn.metrics import mean_absolute_error, r2_score

def train_and_evaluate_model(model, X_train, y_train, X_val, y_val):
    """
    Train a machine learning model and evaluate it on the validation set.

    Parameters:
        model: Scikit-learn compatible model.
        X_train (pd.DataFrame): Training features.
        y_train (pd.Series): Training target.
        X_val (pd.DataFrame): Validation features.
        y_val (pd.Series): Validation target.

    Returns:
        tuple:
            model: Trained model.
            predictions: Predictions on the validation set.
            r2: R² score.
            mae: Mean Absolute Error.
    """

    model.fit(X_train, y_train)

    predictions = model.predict(X_val)

    r2 = r2_score(y_val, predictions)
    mae = mean_absolute_error(y_val, predictions)

    return model, predictions, r2, mae

from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

def tune_random_forest(X_train, y_train, X_val, y_val):
    """
    Tune a Random Forest model using RandomizedSearchCV.
    """

    rf_params = {
        "n_estimators": [200, 300],
        "max_depth": [10, 20],
        "min_samples_split": [5, 10],
    }

    rf_tuned = RandomizedSearchCV(
        estimator=RandomForestRegressor(random_state=42),
        param_distributions=rf_params,
        n_iter=5,
        cv=2,
        scoring="r2",
        n_jobs=-1,          # <-- Use all CPU cores
        random_state=42,
        verbose=2           # <-- Show detailed progress
    )

    rf_tuned.fit(X_train, y_train)

    predictions = rf_tuned.predict(X_val)

    r2 = r2_score(y_val, predictions)
    mae = mean_absolute_error(y_val, predictions)

    return rf_tuned, predictions, rf_tuned.best_params_, r2, mae

from sklearn.metrics import r2_score, mean_absolute_error

def compare_train_validation(model, X_train, y_train, X_val, y_val):
    """
    Compare model performance on the training and validation sets.

    Parameters:
        model: Trained machine learning model.
        X_train (pd.DataFrame): Training features.
        y_train (pd.Series): Training target.
        X_val (pd.DataFrame): Validation features.
        y_val (pd.Series): Validation target.

    Returns:
        tuple:
            train_r2,
            train_mae,
            val_r2,
            val_mae
    """

    # Predictions
    train_pred = model.predict(X_train)
    val_pred = model.predict(X_val)

    # Metrics
    train_r2 = r2_score(y_train, train_pred)
    train_mae = mean_absolute_error(y_train, train_pred)

    val_r2 = r2_score(y_val, val_pred)
    val_mae = mean_absolute_error(y_val, val_pred)

    return train_r2, train_mae, val_r2, val_mae 
 
  
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error

def evaluate_model(model, X_train, y_train, X_val, y_val):
    """
    Evaluate a trained model on the training and validation sets.

    Returns:
        dict: Metrics for the model.
    """

    train_pred = model.predict(X_train)
    val_pred = model.predict(X_val)

    return {
        "R² Train": r2_score(y_train, train_pred),
        "R² Val": r2_score(y_val, val_pred),
        "MAE Train": mean_absolute_error(y_train, train_pred),
        "MAE Val": mean_absolute_error(y_val, val_pred)
    }
from sklearn.metrics import r2_score, mean_absolute_error

def train_and_evaluate_model(model, X_train, y_train, X_eval, y_eval):
    """
    Train a model and evaluate it on any evaluation dataset.

    Parameters:
        model: Scikit-learn compatible model.
        X_train: Training features.
        y_train: Training target.
        X_eval: Evaluation features (validation or test).
        y_eval: Evaluation target.

    Returns:
        tuple:
            model,
            predictions,
            r2,
            mae
    """

    model.fit(X_train, y_train)

    predictions = model.predict(X_eval)

    r2 = r2_score(y_eval, predictions)
    mae = mean_absolute_error(y_eval, predictions)

    return model, predictions, r2, mae

from preprocessing import (
    drop_open_column,
    drop_date_column,
    encode_state_holiday
)

def predict_sales(model, scaler, df):
    """
    Predict sales for new data.

    Closed stores receive a prediction of 0.
    Open stores are preprocessed and predicted by the model.

    Parameters:
        model: Trained model.
        scaler: Fitted StandardScaler.
        df (pd.DataFrame): New data for inference.

    Returns:
        pd.DataFrame: DataFrame with predicted sales.
    """

    df = df.copy()

    # Start with sales = 0
    df["sales"] = 0.0

    # Separate open stores
    open_stores = df[df["open"] == 1].copy()

    # Preprocess
    open_stores = drop_open_column(open_stores)
    open_stores = drop_date_column(open_stores)
    open_stores = encode_state_holiday(open_stores)

    # Scale store_ID
    open_stores[["store_ID"]] = scaler.transform(
        open_stores[["store_ID"]]
    )

    # Predict
    open_stores["sales"] = model.predict(
        open_stores.drop(columns=["sales"])
    )

    # Put predictions back into the original DataFrame
    df.loc[open_stores.index, "sales"] = open_stores["sales"]

    # Convert sales to integers
    df["sales"] = df["sales"].astype(int)

    return df

from sklearn.metrics import r2_score, mean_absolute_error

def evaluate_model_on_dataset(model, X, y):
    """
    Evaluate a trained model on any dataset.

    Parameters:
        model: Trained machine learning model.
        X (pd.DataFrame): Features.
        y (pd.Series): Target values.

    Returns:
        tuple:
            predictions,
            r2,
            mae
    """

    predictions = model.predict(X)

    r2 = r2_score(y, predictions)
    mae = mean_absolute_error(y, predictions)

    return predictions, r2, mae