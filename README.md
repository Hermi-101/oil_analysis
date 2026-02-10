📌 Project Overview
This project, conducted for Birhan Energies, focuses on analyzing the historical fluctuations of Brent crude oil prices (1987–2022). By leveraging Bayesian Change Point Detection, we identify structural breaks in market regimes and correlate them with major global geopolitical events, economic shocks, and OPEC policy changes.
The goal is to provide actionable intelligence for investors, policymakers, and energy companies to better navigate market instability and refine risk management strategies.

📂 Project Structure

├── data/
│   ├── raw/                 # Original Brent price dataset
│   └── external_events.csv  # Curated geopolitical event data
├── docs/
│   └── task1_report.md      # Detailed workflow and assumptions
├── notebooks/
│   └── 01_eda_and_foundations.ipynb  # Phase 1: EDA and Statistical Tests
├── src/
│   ├── api/                 # Flask Backend
│   └── dashboard/           # React Frontend
├── requirements.txt         # Project dependencies
└── README.md

# Brent Oil Dashboard Setup

## 1. Backend (Flask)
- Navigate to `/backend`
- Install dependencies: `pip install flask flask-cors pandas`
- Run the server: `python app.py`
- *Endpoint:* `http://localhost:5000/api/prices`

## 2. Frontend (React)
- Navigate to `/frontend`
- Install dependencies: `npm install`
- Run the app: `npm start`
- *View at:* `http://localhost:3000`

## 3. Key Features
- **Structural Break Visualization:** Red dashed lines indicate change points detected by our Bayesian PyMC model.
- **KPI Indicators:** Real-time display of market volatility and regime shift percentages.
- **Responsive Design:** Dashboard scales for tablet and mobile viewing.
