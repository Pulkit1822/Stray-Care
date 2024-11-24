import React, { useEffect, useState } from 'react';
import { alertsApi } from '../../services/api';

const AlertList= ()=> {
  const [alerts, setAlerts]= useState([]);

  useEffect(()=> {
    const fetchAlerts= async ()=> {
      try {
        const response= await alertsApi.getAlerts();
        setAlerts(response.data.alerts);
      } catch (error) {
        console.error('Error fetching alerts:', error);
      }
    };

    fetchAlerts();
  }, []);

  return (
    <div>
      <h2>Alerts</h2>
      <ul>
        {alerts.map((alert)=> (
          <li key={alert.id}>
            <p>Type: {alert.type}</p>
            <p>Location: {alert.location}</p>
            <p>Severity: {alert.severity}</p>
            <p>Status: {alert.status}</p>
            <p>Description: {alert.description}</p>
            <p>Timestamp: {alert.timestamp}</p>
            {alert.image_url && <img src={alert.image_url} alt="Alert" />}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AlertList;
