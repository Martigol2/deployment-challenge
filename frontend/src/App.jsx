import { useState } from "react";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    store_ID: "",
    day_of_week: "",
    nb_customers_on_day: "",
    promotion: "",
    state_holiday: "",
    school_holiday: "",
    open: "",
    date: "",
  });

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handlePredict = async () => {
    setLoading(true);

    try {
      const response = await fetch(
        "https://deployment-challenge.onrender.com/predict",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            store_ID: Number(formData.store_ID),
            day_of_week: Number(formData.day_of_week),
            nb_customers_on_day: Number(formData.nb_customers_on_day),
            promotion: Number(formData.promotion),
            state_holiday: Number(formData.state_holiday),
            school_holiday: Number(formData.school_holiday),
            open: Number(formData.open),
            date: formData.date,
          }),
        }
      );

      const data = await response.json();

      setPrediction(data[0].sales);
    } catch (error) {
      console.error(error);
      alert("Prediction failed.");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>📈 Sales Prediction</h1>

      <input
        type="number"
        name="store_ID"
        placeholder="Store ID"
        value={formData.store_ID}
        onChange={handleChange}
      />

      <input
        type="number"
        name="day_of_week"
        placeholder="Day of Week"
        value={formData.day_of_week}
        onChange={handleChange}
      />

      <input
        type="number"
        name="nb_customers_on_day"
        placeholder="Number of Customers"
        value={formData.nb_customers_on_day}
        onChange={handleChange}
      />

      <input
        type="number"
        name="promotion"
        placeholder="Promotion (0 or 1)"
        value={formData.promotion}
        onChange={handleChange}
      />

      <input
        type="number"
        name="state_holiday"
        placeholder="State Holiday (0 or 1)"
        value={formData.state_holiday}
        onChange={handleChange}
      />

      <input
        type="number"
        name="school_holiday"
        placeholder="School Holiday (0 or 1)"
        value={formData.school_holiday}
        onChange={handleChange}
      />

      <input
        type="number"
        name="open"
        placeholder="Open (0 or 1)"
        value={formData.open}
        onChange={handleChange}
      />

      <input
        type="date"
        name="date"
        value={formData.date}
        onChange={handleChange}
      />

      <button onClick={handlePredict} disabled={loading}>
        {loading ? "Predicting..." : "Predict"}
      </button>

      {prediction !== null && (
        <h2>Predicted Sales: € {prediction}</h2>
      )}
    </div>
  );
}

export default App;