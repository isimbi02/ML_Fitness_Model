from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

# Load the trained model
model = joblib.load("weight_loss_model.pkl")

# Initialize FastAPI
app = FastAPI()

# Define request model
class InputData(BaseModel):
    days: int

@app.get("/")
def home():
    return {"message": "Welcome to the Weight Loss Prediction API"}

@app.post("/predict/")
def predict_weight_loss(data: InputData):
    prediction = model.predict(np.array([[data.days]]))
    return {"predicted_weight_loss": round(float(prediction[0][0]), 2)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
