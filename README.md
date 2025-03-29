# ML_Fitness_Model
This is a weight loss prediction tool that estimates how many kilograms a person might lose based on their gym attendance (in terms of days attended). The machine learning model, trained using synthetic data, is integrated into the backend built with FastAPI. The frontend uses React.js to collect user input and display the prediction.

Backend:
FastAPI: Web framework for building APIs with Python.
scikit-learn: A library for machine learning, used to train the weight loss prediction model.
Joblib: Used to serialize and load the trained model.
Uvicorn: ASGI server used to serve FastAPI applications.
CORS Middleware: Allows cross-origin requests to enable communication between the frontend and backend.

Frontend:
React.js: JavaScript library for building user interfaces.
Axios: Promise-based HTTP client for making HTTP requests to the backend API.
