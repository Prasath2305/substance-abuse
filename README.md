# Substance Abuse Detection Using Sensor Data

This project aims to detect potential substance abuse based on data collected from various sensors connected to an ESP32 microcontroller. The data is processed using a machine learning (ML) model, and the results are displayed on a Flask web application, indicating whether there's a possibility of substance abuse based on the sensor readings.

## Project Overview

- **Data Collection:** The ESP32 microcontroller collects sensor data that could be indicative of substance abuse.
- **Machine Learning Model:** A basic ML model is trained on this sensor data to predict the likelihood of substance abuse.
- **Web Application:** A Flask web application is used to display the predictions based on real-time sensor data.

## Requirements

To install the required packages, run:

>pip install -r requirements.txt

## Setup and Usage

### Train the ML model by running the `train_model.py` script.

>python model/train_model.py

### Run the Flask Application

>python app.py

## Troubleshooting

- **ParserError:** If you encounter a ParserError while loading the CSV file, ensure that the file is formatted correctly, with consistent fields and no extra commas.
- **Flask App Issues:** If Flask reports errors such as 'before_first_request' not found, ensure your Flask version is up-to-date and check your app’s structure.
