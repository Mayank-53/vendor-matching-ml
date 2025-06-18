# 🔧 Vendor & Technician Matching AI System

An intelligent ML-based matching system that connects customers with the best available technicians or vendors based on **location**, **price**, and **availability**.

> 🚀 Built as part of an AI integration internship project to demonstrate smart service matching using data-driven decision-making.

---

## 📌 Features

- 🏙️ Location-based nearest technician matching
- 💰 Smart price optimization
- ✅ Real-time availability filtering
- 🧠 Scalable ML-ready architecture
- 📱 Ready for frontend/backend integration (JSON output)
- 🔍 Modular and clean Python codebase
- 🧪 Testable via script or Jupyter Notebook

---

## 🗂️ Project Structure

full_ml_vendor_matching_project/
│
├── data/
│ └── technicians.csv # Technician/vendor data
│
├── scripts/
│ └── match_customer.py # Main matching logic
│
├── utils/
│ └── helpers.py # Reusable functions
│
├── notebooks/
│ └── demo_readme.txt # For interactive testing
│
└── README.md # You're here!

---

## 🔍 How It Works

### ✅ Input Required
- Customer's **city**
- Product **brand** and **model**
- Customer **latitude** and **longitude**

### 🔁 Output
A ranked list of best matching technicians based on:
- Proximity (Haversine distance)
- Price
- Availability

```json
{
  "matches": [
    {
      "id": 3,
      "name": "Technician X",
      "distance_km": 4.2,
      "price": 180,
      "score": 92.1,
      "phone": "9876543210"
    }
  ]
}
🧠 Future Enhancements
🤖 Integrate AI model to detect product issue from image

🌍 Live location tracking with Firebase/Map APIs

⭐ Technician ratings and reviews

🔌 REST API or Streamlit interface
