import React from 'react';
import AlertList from './AlertList';
import DetectionMap from './DetectionMap';

const Dashboard= ()=> {
  return (
    <div>
      <h1>Dashboard</h1>
      
      <AlertList />
      <DetectionMap />
    </div>
  );
};

export default Dashboard;
