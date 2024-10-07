import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load data with specified encoding
try:
    data = pd.read_csv('sensor_data.csv', encoding='ISO-8859-1')  # Replace with detected encoding if different
except UnicodeDecodeError as e:
    print("UnicodeDecodeError:", e)
    # Optionally, try a different encoding or handle the error
    data = pd.read_csv('sensor_data.csv', encoding='latin1', errors='replace')

# Features and target
X = data.drop('abuse', axis=1)
y = data['abuse']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model training
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train_scaled, y_train)

# Evaluation
y_pred = clf.predict(X_test_scaled)
print(classification_report(y_test, y_pred))

# Save the model and scaler
joblib.dump(clf, 'substance_abuse_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("Model and scaler have been saved successfully.")
