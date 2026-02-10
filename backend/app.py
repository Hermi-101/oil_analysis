from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import json

app = Flask(__name__)
CORS(app)  # Enables React to talk to Flask

# Load Data
df = pd.read_csv('../data/BrentOilPrices.csv')
events_df = pd.read_csv('../data/oil_events.csv')

@app.route('/api/prices', methods=['GET'])
def get_prices():
    # Return last 500 days for performance, or use date filters
    data = df.tail(500).to_dict(orient='records')
    return jsonify(data)

@app.route('/api/events', methods=['GET'])
def get_events():
    return jsonify(events_df.to_dict(orient='records'))

@app.route('/api/change-points', methods=['GET'])
def get_change_points():
    with open('model_results.json', 'r') as f:
        return jsonify(json.load(f))

if __name__ == '__main__':
    app.run(debug=True, port=5000)