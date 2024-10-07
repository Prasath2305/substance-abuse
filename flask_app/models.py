from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor1 = db.Column(db.Float, nullable=False)
    sensor2 = db.Column(db.Float, nullable=False)
    sensor3 = db.Column(db.Float, nullable=False)
    # Add other sensor fields as needed
    abuse = db.Column(db.Integer, nullable=False)
