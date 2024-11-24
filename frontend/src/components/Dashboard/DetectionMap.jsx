import React, { useEffect, useRef } from 'react';
import { initMap, addMarker } from '../../services/googleMaps';
import { detectionApi } from '../../services/api';

const DetectionMap= ()=> {
  
  const mapRef= useRef(null);


  useEffect(()=> {


    const loadMap= async ()=> {

      const map= await initMap('detection-map');
      const response= await detectionApi.getDetections();
      const detections= response.data.detections;



      detections.forEach((detection)=> {
        const position= {

          lat:parseFloat(detection.location.split(',')[0]),
          lng: parseFloat(detection.location.split(',')[1]),
        };


        addMarker(map, position, {
          title: detection.animal_type,
          label: `${detection.animal_type}   (${detection.confidence * 100}%)`,
        });
      });
    };


    loadMap();

  }, []);

  return <div id="detection-map" style={{  height: '500px', width: '100%' }} />;
};



export default DetectionMap;
