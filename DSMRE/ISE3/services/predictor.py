"""
=========================================================
AI Prediction Service
Loads the ML model once and provides prediction methods
=========================================================
"""

import joblib
import numpy as np

from config import MODEL_PATH, SCALER_PATH

class Predictor:

    def __init__(self):

        print("Loading AI Model...")

        self.model = joblib.load(MODEL_PATH)

        print("Model Loaded Successfully!")

        print("Loading Scaler...")

        self.scaler = joblib.load(SCALER_PATH)

        print("Scaler Loaded Successfully!")

    def predict(self, sensor):

        features = np.array([[
            sensor["Temperature"],
            sensor["Vibration"],
            sensor["Pressure"],
            sensor["Humidity"],
            sensor["RPM"],
            sensor["Current"]
        ]])

        scaled = self.scaler.transform(features)

        prediction = int(self.model.predict(scaled)[0])

        probability = float(
            self.model.predict_proba(scaled)[0][1]
        )

        return prediction, probability

    def get_machine_status(self, probability):

        if probability < 0.30:
            return "Healthy"

        elif probability < 0.70:
            return "Warning"

        else:
            return "Critical"

    def analyze(self, sensor):

        prediction, probability = self.predict(sensor)

        sensor["Prediction"] = prediction

        sensor["FailureProbability"] = round(probability * 100, 2)

        sensor["Status"] = self.get_machine_status(probability)

        return sensor