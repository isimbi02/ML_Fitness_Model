import { useState } from "react";
import axios from "axios";

function App() {
  const [days, setDays] = useState("");
  const [prediction, setPrediction] = useState(null);

  const predict = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/predict/", { days: Number(days) });
      setPrediction(response.data.predicted_weight_loss);
    } catch (error) {
      console.error("Error predicting:", error);
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1 style={{ fontSize: "36px", color: "#333" }}>Gym Weight Loss Predictor</h1>
      <input
        type="number"
        value={days}
        onChange={(e) => setDays(e.target.value)}
        placeholder="Enter days attended"
        style={{
          padding: "10px",
          fontSize: "16px",
          margin: "20px 0",
          borderRadius: "5px",
          border: "1px solid #ccc",
        }}
      />
      <button
        onClick={predict}
        style={{
          padding: "10px 20px",
          fontSize: "16px",
          backgroundColor: "#4CAF50",
          color: "white",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
        }}
      >
        Predict
      </button>
      {prediction !== null && (
        <h2 style={{ marginTop: "20px", color: "#4CAF50" }}>
          Estimated Weight Loss: {prediction} kg
        </h2>
      )}
    </div>
  );
}

export default App;
