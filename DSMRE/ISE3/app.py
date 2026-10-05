"""
=========================================================
Server Rack Digital Twin Dashboard
Flask application and API routes
=========================================================
"""

from flask import Flask, jsonify, render_template, request

from services.simulator import ServerSimulator


# ============================================================
# 1. CREATE FLASK APPLICATION
# ============================================================

app = Flask(__name__)

# Create one shared digital-twin simulator
simulator = ServerSimulator()


# ============================================================
# 2. DASHBOARD ROUTE
# ============================================================

@app.route("/", methods=["GET"])
def home():
    """Display the server rack digital-twin dashboard."""

    return render_template(
        "index.html",
        server=simulator.get_state()
    )


# ============================================================
# 3. LIVE SERVER STATUS
# ============================================================

@app.route("/api/status", methods=["GET"])
def get_status():
    """
    Run one simulation cycle and return:
    - Temperature
    - Fan speed
    - Fan RPM
    - Server status
    - Automatic mode
    - Heat-spike state
    - Event logs
    """

    state = simulator.update()

    return jsonify({
        "success": True,
        **state
    })


# ============================================================
# 4. MANUAL FAN SPEED CONTROL
# ============================================================

@app.route("/api/fan-speed", methods=["POST"])
def set_fan_speed():
    """Set the cooling fan speed manually."""

    data = request.get_json(silent=True)

    if not data or "fan_speed" not in data:
        return jsonify({
            "success": False,
            "error": "fan_speed is required."
        }), 400

    try:
        fan_speed = int(data["fan_speed"])
    except (TypeError, ValueError):
        return jsonify({
            "success": False,
            "error": "Fan speed must be a valid number."
        }), 400

    if not 0 <= fan_speed <= 100:
        return jsonify({
            "success": False,
            "error": "Fan speed must be between 0 and 100."
        }), 400

    state = simulator.set_fan_speed(fan_speed)

    return jsonify({
        "success": True,
        **state
    })


# ============================================================
# 5. AUTOMATIC COOLING CONTROL
# ============================================================

@app.route("/api/auto-mode", methods=["POST"])
def set_auto_mode():
    """Enable or disable automatic fan-speed control."""

    data = request.get_json(silent=True)

    if not data or "enabled" not in data:
        return jsonify({
            "success": False,
            "error": "enabled is required."
        }), 400

    enabled = data["enabled"]

    if not isinstance(enabled, bool):
        return jsonify({
            "success": False,
            "error": "enabled must be true or false."
        }), 400

    state = simulator.set_auto_mode(enabled)

    return jsonify({
        "success": True,
        **state
    })


# ============================================================
# 6. MANUAL HEAT-SPIKE SIMULATION
# ============================================================

@app.route("/api/heat-spike", methods=["POST"])
def trigger_heat_spike():
    """Generate a heat spike for demonstration and testing."""

    state = simulator.trigger_heat_spike()

    return jsonify({
        "success": True,
        "message": "Heat spike triggered successfully.",
        **state
    })


# ============================================================
# 7. RESET DIGITAL TWIN
# ============================================================

@app.route("/api/reset", methods=["POST"])
def reset_simulation():
    """Reset the digital twin to its initial condition."""

    global simulator

    simulator = ServerSimulator()
    state = simulator.get_state()

    return jsonify({
        "success": True,
        "message": "Digital twin simulation reset successfully.",
        **state
    })


# ============================================================
# 8. CURRENT STATE WITHOUT UPDATING
# ============================================================

@app.route("/api/current-state", methods=["GET"])
def current_state():
    """Return the current state without running a new cycle."""

    return jsonify({
        "success": True,
        **simulator.get_state()
    })


# ============================================================
# 9. HEALTH CHECK
# ============================================================

@app.route("/api/health", methods=["GET"])
def health_check():
    """Check whether the Flask server is running."""

    return jsonify({
        "success": True,
        "application": "Server Rack Digital Twin",
        "status": "Online"
    })


# ============================================================
# 10. ERROR HANDLERS
# ============================================================

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        "success": False,
        "error": "Requested route was not found."
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": "Method not allowed for this route."
    }), 405


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": "An internal server error occurred."
    }), 500


# ============================================================
# 11. START APPLICATION
# ============================================================

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
        threaded=True
    )