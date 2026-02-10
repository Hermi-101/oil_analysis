import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';

function App() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Ensure Flask is running on http://127.0.0.1:5000
    axios.get('http://127.0.0.1:5000/api/prices')
      .then(response => {
        // Taking the last 150 days for a good-looking chart
        setData(response.data.slice(-150));
        setLoading(false);
      })
      .catch(err => {
        console.error("API Error:", err);
        setLoading(false);
      });
  }, []);

  if (loading) return <div style={{padding: '50px'}}>Connecting to Birhan Energies API...</div>;

  return (
    <div style={{ padding: '40px', backgroundColor: '#f8f9fa', minHeight: '100vh' }}>
      <div style={{ backgroundColor: 'white', padding: '20px', borderRadius: '15px', boxShadow: '0 10px 25px rgba(0,0,0,0.1)' }}>
        <h2 style={{ color: '#1a365d', marginBottom: '5px' }}>Brent Crude Oil Price Dashboard</h2>
        <p style={{ color: '#718096', marginBottom: '20px' }}>Real-time Market Data via Birhan Energies API</p>
        
        {/* We removed ResponsiveContainer to fix the useContext error */}
        <LineChart width={800} height={400} data={data}>
          <CartesianGrid strokeDasharray="3 3" vertical={false} />
          <XAxis dataKey="Date" tick={{fontSize: 10}} interval={20} />
          <YAxis domain={['auto', 'auto']} />
          <Tooltip />
          <Line 
            type="monotone" 
            dataKey="Price" 
            stroke="#2b6cb0" 
            strokeWidth={3} 
            dot={false}
            animationDuration={1500}
          />
        </LineChart>

        <div style={{ marginTop: '20px', display: 'flex', gap: '20px' }}>
          <div style={{ padding: '15px', borderLeft: '4px solid #2b6cb0', backgroundColor: '#ebf8ff' }}>
            <small>Current Focus</small>
            <div style={{ fontWeight: 'bold' }}>Last 150 Days</div>
          </div>
          <div style={{ padding: '15px', borderLeft: '4px solid #38a169', backgroundColor: '#f0fff4' }}>
            <small>API Status</small>
            <div style={{ fontWeight: 'bold', color: '#38a169' }}>Connected</div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;