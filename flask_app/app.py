from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, SensorData
import joblib
import numpy as np

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sensor_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Load the trained model and scaler
model = joblib.load('substance_abuse_model.pkl')
scaler = joblib.load('scaler.pkl')

# @app.before_first_request
# def create_tables():
#     db.create_all()

@app.route('/')
def index():
    data = SensorData.query.all()
    return render_template('index.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    # Extract sensor data from the form or request
    try:
        sensor1 = float(request.form['sensor1'])
        sensor2 = float(request.form['sensor2'])
        sensor3 = float(request.form['sensor3'])
        # Add other sensors as needed
    except (ValueError, KeyError):
        return "Invalid input", 400

    # Prepare data for prediction
    input_features = np.array([[sensor1, sensor2, sensor3]])  # Add other sensors
    input_scaled = scaler.transform(input_features)
    prediction = model.predict(input_scaled)[0]

    # Store the data with prediction
    new_entry = SensorData(
        sensor1=sensor1,
        sensor2=sensor2,
        sensor3=sensor3,
        # Add other sensors
        abuse=prediction
    )
    db.session.add(new_entry)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
