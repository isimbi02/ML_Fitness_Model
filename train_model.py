import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Generate synthetic data
np.random.seed(42)
days_attended = np.random.randint(1, 100, 100).reshape(-1, 1)
weight_loss = days_attended * 0.1 + np.random.normal(0, 1, (100, 1))  # Assumed trend

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(days_attended, weight_loss, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "weight_loss_model.pkl")
print("Model saved successfully!")
