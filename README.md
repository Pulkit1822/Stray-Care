<p align="center">
  <a href="https://github.com/Pulkit1822/Stray-Care">
    <img src="https://github.com/Pulkit1822/Stray-Care/blob/main/assets/logo.jpg" height="128">
  </a>
  <h1 align="center">Stray Care</h1>
</p>

## Project Description

Welcome to the Stray Care Project! This solo project aims to address the significant dangers posed by stray cattle 🐄 and other animals 🦊 on roadways. These incidents often result in injuries, fatalities, and property damage 🏥🚑. My goal is to create innovative solutions that integrate technology and infrastructure to detect animals on the road, alert drivers, and manage animal movement effectively. Potential solutions involve the use of sensors, GPS tracking, driver notification systems, and physical deterrents. Ultimately, I aim to enhance road safety, reduce accidents, and safeguard both drivers and animals 🦺. Note that I didn't have any ML models for animal detection and risk prediction, so I haven't included any samples(I'm not an ML person 😬).

## Problem Statement

Accidents caused by stray cattle 🐄 and other animals 🦊 on roadways present significant dangers, often resulting in injuries, fatalities, and property damage 🏥🚑. The challenge is to create innovative solutions that integrate technology and infrastructure to detect animals on the road, alert drivers, and manage animal movement effectively. Potential solutions could involve the use of sensors, GPS tracking, driver notification systems, and physical deterrents. The ultimate goal is to enhance road safety, reduce accidents, and safeguard both drivers and animals 🦺.

> > View full problem statement here: [Tap to view](https://save-the-stray-challenge.devfolio.co/overview)

## System Architecture

![System Architecture](https://github.com/Pulkit1822/Stray-Care/blob/main/assets/system-architecture.png)

## Detailed Project Explanation

### Overview

The Stray Care Project is designed to detect stray animals on roadways and alert drivers in real-time. The system consists of multiple components that work together seamlessly to achieve this goal.

### Backend

The backend is built using Flask, a lightweight web framework for Python. It handles API requests, processes data, and communicates with the frontend and hardware components.

#### Key Files

- `app.py`: Initializes the Flask application, sets up extensions, and registers API blueprints.
- `config.py`: Contains configuration settings for the application.
- `models/alert.py`: Defines the Alert model for storing alert data in the database.
- `models/detection.py`: Defines the Detection model for storing detection data in the database.
- `routes/alerts.py`: Handles API routes related to alerts.
- `routes/detection.py`: Handles API routes related to detections.
- `services/alert_service.py`: Contains business logic for managing alerts.
- `services/detection_service.py`: Contains business logic for analyzing images and processing streams.

### Frontend

The frontend is built using React, a popular JavaScript library for building user interfaces. It provides a dashboard for viewing alerts and detections, as well as a map for visualizing detection locations.

#### Key Files

- `App.jsx`: The main entry point of the React application.
- `Dashboard/AlertList.jsx`: Displays a list of alerts.
- `Dashboard/DetectionMap.jsx`: Displays a map with detection markers.
- `services/api.js`: Contains functions for making API requests.

### Hardware

The hardware components include sensors, cameras, and alert modules. These components are connected to a Raspberry Pi, which processes data and communicates with the backend.

#### Key Files

- `alert_module/main.py`: Controls the alert module, which triggers visual and auditory alerts.
- `camera_module/main.py`: Captures and processes images from the camera.
- `sensor_module/main.py`: Measures distance using ultrasonic sensors and publishes alerts.

## Why My Solution is Better

My solution stands out from existing solutions due to its comprehensive approach and integration of multiple technologies. Here are some key advantages:

1. **Real-time Detection**: My system provides real-time detection and alerts, ensuring timely responses to potential hazards.
2. **Comprehensive Coverage**: By using a combination of sensors, cameras, and GPS tracking, I achieve comprehensive coverage of roadways.
3. **Scalability**: The modular design of my system allows for easy scalability and integration with existing infrastructure.
4. **User-Friendly Interface**: The React-based frontend provides a user-friendly interface for monitoring alerts and detections.
5. **Open Source**: My project is open source, allowing for community contributions and continuous improvement.

## Technologies Used

- **Backend**: Flask, SQLAlchemy, Flask-JWT-Extended, Flask-CORS
- **Frontend**: React, React Router, Axios, Google Maps API
- **Hardware**: Raspberry Pi, Ultrasonic Sensors, Cameras, MQTT
- **Database**: SQLite (can be replaced with other databases)
- **Cloud**: Google Cloud Platform (for hosting and additional services)

## Hackathon Participation

This project was made for the hackathon - IIIT NR presents Save The Stray Challenge - online challenge 2024.

## Detailed Explanation of Important Code Files

### `backend/api/models/alert.py`

This file defines the Alert model, which is used to store alert data in the database. Each alert has attributes such as type, location, severity, timestamp, status, description, and image URL. The `to_dict` method converts the alert object to a dictionary for easy serialization.

### `backend/api/models/detection.py`

This file defines the Detection model, which is used to store detection data in the database. Each detection has attributes such as animal type, confidence, location, timestamp, image URL, and metadata. The `to_dict` method converts the detection object to a dictionary for easy serialization.

### `backend/api/routes/alerts.py`

This file handles API routes related to alerts. It includes routes for getting all alerts, getting a specific alert by ID, and creating a new alert. The routes are protected by JWT authentication.

### `backend/api/routes/detection.py`

This file handles API routes related to detections. It includes routes for analyzing images and processing streams. The routes are protected by JWT authentication.

### `backend/services/alert_service.py`

This file contains business logic for managing alerts. It includes methods for creating, retrieving, and updating alerts. The methods interact with the database using SQLAlchemy.

### `backend/services/detection_service.py`

This file contains business logic for analyzing images and processing streams. It includes methods for analyzing images, processing stream data, and saving detections to the database.

### `frontend/src/components/Dashboard/AlertList.jsx`

This file defines the AlertList component, which displays a list of alerts. It fetches alerts from the backend API and renders them in a list format.

### `frontend/src/components/Dashboard/DetectionMap.jsx`

This file defines the DetectionMap component, which displays a map with detection markers. It initializes the Google Map, fetches detection data from the backend API, and adds markers to the map.

## Conclusion

Thank you for checking out the Stray Care Project! I hope this project contributes to enhancing road safety and protecting both drivers and animals. If you have any questions or suggestions, feel free to reach out. Let's make the roads safer together! 🚗🛣️🐾

## Acknowledgements

I would like to extend my heartfelt thanks to IIIT NR for organizing the 'Save The Stray Challenge' November 2024. Participating in this hackathon has been an incredible experience, and I am grateful for the opportunity to contribute to such a meaningful cause.

## Feedback

If you have any feedback, suggestions, or questions regarding this repository, please feel free to open an issue or contact me below on any of the platforms you prefer 😊
<br/>
<p align="center">
  <a href="https://pulkitmathur.tech/"><img src="https://github.com/Pulkit1822/Pulkit1822/blob/main/animated-icons/pic.jpeg" alt="portfolio" width="32"></a>&nbsp;&nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/pulkitkmathur/"><img src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/Linkedin.svg" alt="Linkedin Logo" width="32"></a>&nbsp;&nbsp;&nbsp;
  <a href="mailto:pulkitmathur.me@gmail.com"><img src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/Gmail.svg" alt="Gmail logo" height="32"></a>&nbsp;&nbsp;&nbsp;
  <a href="https://www.instagram.com/pulkitkumarmathur/"><img src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/Instagram.svg" alt="Instagram Logo" width="32"></a>&nbsp;&nbsp;&nbsp;
  <a href="https://in.pinterest.com/pulkitkumarmathur/"><img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Pinterest-logo.png?20160129083321" alt="Pinterest Logo" width="32"></a>&nbsp;&nbsp;&nbsp;
  <a href="https://twitter.com/pulkitkmathur"><img src="https://upload.wikimedia.org/wikipedia/commons/5/57/X_logo_2023_%28white%29.png" alt="Twitter Logo" width="32"></a>&nbsp;&nbsp;&nbsp;
</p>

Happy learning and coding!

---

If you find this repository useful, don't forget to star it! ⭐️

### Written by [Pulkit](https://github.com/Pulkit1822)
# Stray-Care
