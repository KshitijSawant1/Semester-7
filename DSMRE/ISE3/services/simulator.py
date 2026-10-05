"""
Digital Twin Server Rack Simulator

Simulates:
- Server temperature
- Random heat spikes
- Fan speed and RPM
- Automatic cooling
- Server health status
- Event logging
"""

import random
from datetime import datetime
from threading import Lock


class ServerSimulator:

    def __init__(self):
        self.lock = Lock()

        self.temperature = 38.0
        self.fan_speed = 40
        self.rpm = 1700

        self.status = "Stable"
        self.auto_mode = True
        self.heat_spike = False

        self.logs = []

        self.add_log(
            "Digital twin simulation started",
            "success"
        )

    # --------------------------------------------------
    # Event logging
    # --------------------------------------------------

    def add_log(self, message, level="info"):
        log = {
            "time": datetime.now().strftime("%H:%M:%S"),
            "message": message,
            "level": level
        }

        self.logs.insert(0, log)

        # Keep only latest 25 events
        self.logs = self.logs[:25]

    # --------------------------------------------------
    # Server status
    # --------------------------------------------------

    def calculate_status(self):
        if self.temperature >= 75:
            return "Critical"

        if self.temperature >= 55:
            return "Warning"

        return "Stable"

    # --------------------------------------------------
    # Automatic fan controller
    # --------------------------------------------------

    def calculate_auto_fan_speed(self):
        if self.temperature >= 75:
            return 100

        if self.temperature >= 65:
            return 90

        if self.temperature >= 55:
            return 75

        if self.temperature >= 45:
            return 60

        if self.temperature >= 38:
            return 45

        return 30

    # --------------------------------------------------
    # Random heat generation
    # --------------------------------------------------

    def generate_heat(self):
        """
        Simulates normal server heat and occasional spikes.
        """

        # Approximately 10% chance per simulation cycle
        spike_occurs = random.random() < 0.10

        if spike_occurs:
            spike = random.uniform(5.0, 12.0)

            self.temperature += spike
            self.heat_spike = True

            self.add_log(
                f"Heat spike detected: +{spike:.1f}°C",
                "danger"
            )

        else:
            self.heat_spike = False

            # Normal heat from server workload
            normal_heat = random.uniform(0.4, 1.4)

            self.temperature += normal_heat

    # --------------------------------------------------
    # Cooling calculation
    # --------------------------------------------------

    def apply_cooling(self):
        """
        Higher fan speed produces greater cooling.
        """

        cooling_effect = self.fan_speed * 0.035

        # Small environmental variation
        environmental_effect = random.uniform(-0.15, 0.20)

        self.temperature -= cooling_effect
        self.temperature += environmental_effect

    # --------------------------------------------------
    # RPM calculation
    # --------------------------------------------------

    def calculate_rpm(self):
        if self.fan_speed == 0:
            return 0

        return int(500 + self.fan_speed * 30)

    # --------------------------------------------------
    # One simulation cycle
    # --------------------------------------------------

    def update(self):
        with self.lock:

            old_status = self.status
            old_fan_speed = self.fan_speed
            previous_temperature = self.temperature

            # Generate server heat
            self.generate_heat()

            # Automatic cooling controller
            if self.auto_mode:
                required_speed = self.calculate_auto_fan_speed()

                self.fan_speed = required_speed

                if required_speed != old_fan_speed:
                    self.add_log(
                        (
                            "Automatic cooling adjusted "
                            f"fan speed to {required_speed}%"
                        ),
                        "warning"
                    )

            # Apply fan cooling
            self.apply_cooling()

            # Restrict values to realistic range
            self.temperature = max(
                25.0,
                min(95.0, self.temperature)
            )

            self.temperature = round(
                self.temperature,
                1
            )

            self.rpm = self.calculate_rpm()
            self.status = self.calculate_status()

            # Log status change
            if self.status != old_status:
                if self.status == "Critical":
                    level = "danger"
                elif self.status == "Warning":
                    level = "warning"
                else:
                    level = "success"

                self.add_log(
                    f"Server status changed to {self.status}",
                    level
                )

            # Log successful recovery
            if (
                previous_temperature >= 55
                and self.temperature < 55
            ):
                self.add_log(
                    "Server temperature returned to safe range",
                    "success"
                )

            return self.get_state()

    # --------------------------------------------------
    # Manual fan control
    # --------------------------------------------------

    def set_fan_speed(self, speed):
        with self.lock:

            speed = int(speed)
            speed = max(0, min(100, speed))

            self.auto_mode = False
            self.fan_speed = speed
            self.rpm = self.calculate_rpm()

            self.add_log(
                f"Manual fan speed set to {speed}%",
                "info"
            )

            return self.get_state()

    # --------------------------------------------------
    # Automatic mode
    # --------------------------------------------------

    def set_auto_mode(self, enabled):
        with self.lock:

            self.auto_mode = bool(enabled)

            if self.auto_mode:
                self.fan_speed = self.calculate_auto_fan_speed()
                message = "Automatic cooling enabled"
                level = "success"
            else:
                message = "Automatic cooling disabled"
                level = "warning"

            self.rpm = self.calculate_rpm()

            self.add_log(message, level)

            return self.get_state()

    # --------------------------------------------------
    # Simulate a manual heat spike
    # --------------------------------------------------

    def trigger_heat_spike(self):
        with self.lock:

            spike = random.uniform(8.0, 15.0)

            self.temperature += spike
            self.temperature = min(
                self.temperature,
                95.0
            )

            self.temperature = round(
                self.temperature,
                1
            )

            self.heat_spike = True
            self.status = self.calculate_status()

            self.add_log(
                f"Manual heat spike triggered: +{spike:.1f}°C",
                "danger"
            )

            return self.get_state()

    # --------------------------------------------------
    # Return current state
    # --------------------------------------------------

    def get_state(self):
        return {
            "temperature": self.temperature,
            "fan_speed": self.fan_speed,
            "rpm": self.rpm,
            "status": self.status,
            "auto_mode": self.auto_mode,
            "heat_spike": self.heat_spike,
            "logs": self.logs
        }