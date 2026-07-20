from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Body
from utils import load_model
from functions import predict_sales
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://deployment-challenge.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = load_model("models/xgboost.pkl")
scaler = load_model("models/scaler.pkl")


@app.get("/")
def home():
    return {
        "message": "Deployment Challenge API is running!"
    }


@app.post("/predict")
def predict(data: dict = Body(...)):

    # Convert JSON to DataFrame
    df = pd.DataFrame([data])

    # Predict sales
    prediction = predict_sales(
        model,
        scaler,
        df
    )

    # Return prediction
    return prediction.to_dict(orient="records")