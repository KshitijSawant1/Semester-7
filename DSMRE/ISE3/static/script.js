/* =========================================================
   DOM ELEMENTS
========================================================= */

const fanSlider = document.getElementById("fanSpeed");
const fanSliderProgress = document.getElementById(
    "fanSliderProgress"
);

const fan = document.getElementById("fan");
const serverRack = document.getElementById("serverRack");

const fanSpeedValue = document.getElementById(
    "fanSpeedValue"
);

const controlSpeedValue = document.getElementById(
    "controlSpeedValue"
);

const sliderValue = document.getElementById(
    "sliderValue"
);

const coolingStateValue = document.getElementById(
    "coolingStateValue"
);

const rpmValue = document.getElementById("rpmValue");

const temperatureValue = document.getElementById(
    "temperatureValue"
);

const temperatureProgress = document.getElementById(
    "temperatureProgress"
);

const fanStatus = document.getElementById("fanStatus");

const controlModeBadge = document.getElementById(
    "controlModeBadge"
);

const autoModeButton = document.getElementById(
    "autoModeButton"
);

const heatSpikeButton = document.getElementById(
    "heatSpikeButton"
);

const toggleSimulationButton = document.getElementById(
    "toggleSimulationButton"
);

const modeMessage = document.getElementById(
    "modeMessage"
);

const eventLog = document.getElementById("eventLog");
const logCount = document.getElementById("logCount");

const heatSpikeAlert = document.getElementById(
    "heatSpikeAlert"
);

const chartTemperatureValue = document.getElementById(
    "chartTemperatureValue"
);

const chartFanSpeedValue = document.getElementById(
    "chartFanSpeedValue"
);

const chartRpmValue = document.getElementById(
    "chartRpmValue"
);

const serverChartCanvas = document.getElementById(
    "serverChart"
);


/* =========================================================
   APPLICATION STATE
========================================================= */

let automaticMode = true;
let simulationEnabled = true;
let isUpdatingFan = false;

let displayedFanSpeed = 0;
let fanAnimationFrame = null;

let serverChart = null;

const chartLabels = [];
const temperatureHistory = [];
const fanSpeedHistory = [];


/* =========================================================
   SMOOTH NUMBER ANIMATION
========================================================= */

function animateNumber(
    element,
    targetValue,
    options = {}
) {
    if (!element) {
        return;
    }

    const {
        duration = 700,
        decimals = 0,
        suffix = ""
    } = options;

    const startValue =
        Number.parseFloat(element.textContent) || 0;

    const target = Number(targetValue);

    if (!Number.isFinite(target)) {
        return;
    }

    const difference = target - startValue;
    const startTime = performance.now();

    element.classList.add("metric-updating");

    function animate(currentTime) {
        const elapsed = currentTime - startTime;

        const progress = Math.min(
            elapsed / duration,
            1
        );

        const easedProgress =
            1 - Math.pow(1 - progress, 3);

        const current =
            startValue + difference * easedProgress;

        element.textContent =
            `${current.toFixed(decimals)}${suffix}`;

        if (progress < 1) {
            requestAnimationFrame(animate);
        } else {
            element.textContent =
                `${target.toFixed(decimals)}${suffix}`;

            element.classList.remove(
                "metric-updating"
            );
        }
    }

    requestAnimationFrame(animate);
}


/* =========================================================
   FAN ANIMATION
========================================================= */

function updateFanAnimation(targetSpeed) {
    if (!fan) {
        return;
    }

    const safeTarget = Math.min(
        100,
        Math.max(0, Number(targetSpeed))
    );

    if (fanAnimationFrame) {
        cancelAnimationFrame(fanAnimationFrame);
    }

    function animateSpeed() {
        const difference =
            safeTarget - displayedFanSpeed;

        if (Math.abs(difference) < 0.3) {
            displayedFanSpeed = safeTarget;
        } else {
            displayedFanSpeed += difference * 0.08;
        }

        if (displayedFanSpeed <= 0.3) {
            fan.style.animationPlayState = "paused";
        } else {
            fan.style.animationPlayState = "running";

            const duration = Math.max(
                0.12,
                2.4 - displayedFanSpeed * 0.022
            );

            fan.style.setProperty(
                "--fan-duration",
                `${duration}s`
            );
        }

        if (
            Math.abs(
                safeTarget - displayedFanSpeed
            ) >= 0.3
        ) {
            fanAnimationFrame =
                requestAnimationFrame(
                    animateSpeed
                );
        }
    }

    animateSpeed();
}


/* =========================================================
   FAN-SPEED PROGRESS BAR
========================================================= */

function updateFanSliderProgress(speed) {
    if (!fanSliderProgress) {
        return;
    }

    const safeSpeed = Math.min(
        100,
        Math.max(0, Number(speed))
    );

    fanSliderProgress.style.width =
        `${safeSpeed}%`;

    fanSliderProgress.className =
        "fan-slider-progress";

    if (safeSpeed >= 90) {
        fanSliderProgress.classList.add(
            "maximum-speed"
        );
    } else if (safeSpeed >= 70) {
        fanSliderProgress.classList.add(
            "high-speed"
        );
    } else if (safeSpeed >= 35) {
        fanSliderProgress.classList.add(
            "medium-speed"
        );
    }
}


/* =========================================================
   TEMPERATURE BAR
========================================================= */

function updateTemperatureBar(temperature) {
    if (!temperatureProgress) {
        return;
    }

    const safeTemperature = Math.min(
        100,
        Math.max(0, Number(temperature))
    );

    temperatureProgress.style.width =
        `${safeTemperature}%`;

    if (safeTemperature >= 70) {
        temperatureProgress.className =
            "temperature-progress critical-bar";
    } else if (safeTemperature >= 55) {
        temperatureProgress.className =
            "temperature-progress warning-bar";
    } else {
        temperatureProgress.className =
            "temperature-progress stable-bar";
    }
}


/* =========================================================
   EVENT LOG
========================================================= */

function escapeHtml(value) {
    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}


function updateLogs(logs = []) {
    if (!eventLog || !logCount) {
        return;
    }

    logCount.textContent =
        `${logs.length} Event${logs.length === 1 ? "" : "s"}`;

    if (logs.length === 0) {
        eventLog.innerHTML = `
            <div class="empty-log">
                No events recorded.
            </div>
        `;

        return;
    }

    eventLog.innerHTML = logs.map((log) => {
        const level = escapeHtml(
            log.level || "info"
        );

        const time = escapeHtml(
            log.time || "--:--:--"
        );

        const message = escapeHtml(
            log.message || "Unknown event"
        );

        return `
            <div class="log-item ${level}">
                <span class="log-time">
                    ${time}
                </span>

                <span class="log-message">
                    ${message}
                </span>
            </div>
        `;
    }).join("");
}


/* =========================================================
   LIVE CHART
========================================================= */

function initializeChart() {
    if (
        !serverChartCanvas ||
        typeof Chart === "undefined"
    ) {
        return;
    }

    serverChart = new Chart(
        serverChartCanvas,
        {
            type: "line",

            data: {
                labels: chartLabels,

                datasets: [
                    {
                        label: "Temperature (°C)",
                        data: temperatureHistory,
                        borderColor: "#ef4444",
                        backgroundColor:
                            "rgba(239, 68, 68, 0.10)",
                        borderWidth: 2,
                        tension: 0.35,
                        fill: true,
                        pointRadius: 2,
                        pointHoverRadius: 5,
                        yAxisID: "temperatureAxis"
                    },
                    {
                        label: "Fan Speed (%)",
                        data: fanSpeedHistory,
                        borderColor: "#0ea5e9",
                        backgroundColor:
                            "rgba(14, 165, 233, 0.08)",
                        borderWidth: 2,
                        tension: 0.35,
                        fill: false,
                        pointRadius: 2,
                        pointHoverRadius: 5,
                        yAxisID: "fanAxis"
                    }
                ]
            },

            options: {
                responsive: true,
                maintainAspectRatio: false,
                animation: {
                    duration: 500
                },
                interaction: {
                    intersect: false,
                    mode: "index"
                },
                plugins: {
                    legend: {
                        position: "top"
                    },
                    tooltip: {
                        callbacks: {
                            label(context) {
                                const value =
                                    context.parsed.y;

                                if (
                                    context.dataset.yAxisID ===
                                    "temperatureAxis"
                                ) {
                                    return ` Temperature: ${value}°C`;
                                }

                                return ` Fan Speed: ${value}%`;
                            }
                        }
                    }
                },
                scales: {
                    x: {
                        grid: {
                            color:
                                "rgba(148, 163, 184, 0.15)"
                        },
                        ticks: {
                            color: "#64748b"
                        }
                    },
                    temperatureAxis: {
                        type: "linear",
                        position: "left",
                        suggestedMin: 20,
                        suggestedMax: 90,
                        title: {
                            display: true,
                            text: "Temperature (°C)"
                        },
                        grid: {
                            color:
                                "rgba(148, 163, 184, 0.15)"
                        },
                        ticks: {
                            color: "#64748b"
                        }
                    },
                    fanAxis: {
                        type: "linear",
                        position: "right",
                        min: 0,
                        max: 100,
                        title: {
                            display: true,
                            text: "Fan Speed (%)"
                        },
                        grid: {
                            drawOnChartArea: false
                        },
                        ticks: {
                            color: "#64748b"
                        }
                    }
                }
            }
        }
    );
}


function updateChart(data) {
    if (!serverChart) {
        return;
    }

    const currentTime =
        new Date().toLocaleTimeString(
            [],
            {
                hour: "2-digit",
                minute: "2-digit",
                second: "2-digit"
            }
        );

    chartLabels.push(currentTime);

    temperatureHistory.push(
        Number(data.temperature)
    );

    fanSpeedHistory.push(
        Number(data.fan_speed)
    );

    const maximumPoints = 25;

    if (chartLabels.length > maximumPoints) {
        chartLabels.shift();
        temperatureHistory.shift();
        fanSpeedHistory.shift();
    }

    serverChart.update();
}


/* =========================================================
   UPDATE COMPLETE DASHBOARD
========================================================= */

function updateDashboard(data) {
    if (!data) {
        return;
    }

    const temperature = Number(data.temperature);
    const fanSpeed = Number(data.fan_speed);
    const rpm = Number(data.rpm);

    if (serverRack) {
        serverRack.classList.toggle(
            "heat-warning",
            temperature >= 55 ||
            Boolean(data.heat_spike)
        );
    }

    animateNumber(
        temperatureValue,
        temperature,
        {
            duration: 900,
            decimals: 1
        }
    );

    animateNumber(
        fanSpeedValue,
        fanSpeed,
        {
            duration: 700,
            decimals: 0,
            suffix: "%"
        }
    );

    animateNumber(
        controlSpeedValue,
        fanSpeed,
        {
            duration: 700,
            decimals: 0,
            suffix: "%"
        }
    );

    animateNumber(
        sliderValue,
        fanSpeed,
        {
            duration: 700,
            decimals: 0,
            suffix: "%"
        }
    );

    animateNumber(
        rpmValue,
        rpm,
        {
            duration: 700,
            decimals: 0,
            suffix: " RPM"
        }
    );

    animateNumber(
        chartTemperatureValue,
        temperature,
        {
            duration: 700,
            decimals: 1,
            suffix: "°C"
        }
    );

    animateNumber(
        chartFanSpeedValue,
        fanSpeed,
        {
            duration: 700,
            decimals: 0,
            suffix: "%"
        }
    );

    animateNumber(
        chartRpmValue,
        rpm,
        {
            duration: 700,
            decimals: 0
        }
    );

    if (
        fanSlider &&
        !isUpdatingFan
    ) {
        fanSlider.value = fanSpeed;
    }

    updateFanSliderProgress(fanSpeed);

    if (fanStatus) {
        fanStatus.textContent =
            data.status || "Unknown";

        fanStatus.className =
            `status ${String(
                data.status || "unknown"
            ).toLowerCase()}`;
    }

    automaticMode = Boolean(data.auto_mode);

    simulationEnabled =
        data.simulation_enabled !== false;

    if (autoModeButton) {
        autoModeButton.textContent =
            automaticMode
                ? "Disable Automatic Cooling"
                : "Enable Automatic Cooling";
    }

    if (controlModeBadge) {
        controlModeBadge.textContent =
            automaticMode
                ? "Auto Mode"
                : "Manual Mode";

        controlModeBadge.className =
            automaticMode
                ? "control-mode-badge auto"
                : "control-mode-badge manual";
    }

    if (coolingStateValue) {
        coolingStateValue.textContent =
            fanSpeed > 0
                ? "Active"
                : "Stopped";
    }

    if (toggleSimulationButton) {
        toggleSimulationButton.textContent =
            simulationEnabled
                ? "Disable Heat Spike Simulation"
                : "Enable Heat Spike Simulation";

        toggleSimulationButton.classList.toggle(
            "simulation-disabled",
            !simulationEnabled
        );
    }

    if (modeMessage) {
        if (!simulationEnabled) {
            modeMessage.textContent =
                automaticMode
                    ? "Automatic cooling is active. Random heat spikes are disabled."
                    : "Manual cooling is active. Random heat spikes are disabled.";
        } else {
            modeMessage.textContent =
                automaticMode
                    ? "Automatic cooling is controlling fan speed."
                    : "Manual cooling mode is active.";
        }
    }

    if (heatSpikeAlert) {
        heatSpikeAlert.classList.toggle(
            "visible",
            Boolean(data.heat_spike)
        );
    }

    updateFanAnimation(fanSpeed);
    updateTemperatureBar(temperature);

    if (Array.isArray(data.logs)) {
        updateLogs(data.logs);
    }

    updateChart(data);
}


/* =========================================================
   API HELPER
========================================================= */

async function requestJson(
    url,
    options = {}
) {
    const response = await fetch(
        url,
        options
    );

    let data;

    try {
        data = await response.json();
    } catch {
        data = {};
    }

    if (!response.ok) {
        throw new Error(
            data.error ||
            `Request failed with status ${response.status}`
        );
    }

    return data;
}


/* =========================================================
   GET LIVE DIGITAL-TWIN STATUS
========================================================= */

async function fetchServerStatus() {
    try {
        const data = await requestJson(
            "/api/status"
        );

        updateDashboard(data);
    } catch (error) {
        console.error(
            "Status Error:",
            error
        );

        if (modeMessage) {
            modeMessage.textContent =
                "Unable to communicate with Flask server.";
        }
    }
}


/* =========================================================
   MANUAL FAN SPEED CONTROL
========================================================= */

async function setFanSpeed(speed) {
    try {
        const data = await requestJson(
            "/api/fan-speed",
            {
                method: "POST",
                headers: {
                    "Content-Type":
                        "application/json"
                },
                body: JSON.stringify({
                    fan_speed: Number(speed)
                })
            }
        );

        updateDashboard(data);
    } catch (error) {
        console.error(
            "Fan Speed Error:",
            error
        );

        if (modeMessage) {
            modeMessage.textContent =
                "Unable to update fan speed.";
        }
    }
}


/* =========================================================
   AUTOMATIC COOLING CONTROL
========================================================= */

async function toggleAutoMode() {
    const requestedMode =
        !automaticMode;

    if (autoModeButton) {
        autoModeButton.disabled = true;
    }

    try {
        const data = await requestJson(
            "/api/auto-mode",
            {
                method: "POST",
                headers: {
                    "Content-Type":
                        "application/json"
                },
                body: JSON.stringify({
                    enabled: requestedMode
                })
            }
        );

        updateDashboard(data);
    } catch (error) {
        console.error(
            "Auto Mode Error:",
            error
        );

        if (modeMessage) {
            modeMessage.textContent =
                "Unable to change automatic cooling mode.";
        }
    } finally {
        if (autoModeButton) {
            autoModeButton.disabled = false;
        }
    }
}


/* =========================================================
   MANUAL HEAT-SPIKE SIMULATION
========================================================= */

async function triggerHeatSpike() {
    if (!heatSpikeButton) {
        return;
    }

    heatSpikeButton.disabled = true;

    heatSpikeButton.textContent =
        "Generating Heat Spike...";

    try {
        const data = await requestJson(
            "/api/heat-spike",
            {
                method: "POST"
            }
        );

        updateDashboard(data);

        if (modeMessage) {
            modeMessage.textContent =
                "Manual heat spike generated successfully.";
        }
    } catch (error) {
        console.error(
            "Heat Spike Error:",
            error
        );

        if (modeMessage) {
            modeMessage.textContent =
                "Unable to generate the heat spike.";
        }
    } finally {
        setTimeout(() => {
            heatSpikeButton.disabled = false;

            heatSpikeButton.textContent =
                "Simulate Heat Spike";
        }, 800);
    }
}


/* =========================================================
   TOGGLE RANDOM HEAT-SPIKE SIMULATION
========================================================= */

async function toggleHeatSimulation() {
    if (!toggleSimulationButton) {
        return;
    }

    toggleSimulationButton.disabled = true;

    try {
        const data = await requestJson(
            "/api/toggle-simulation",
            {
                method: "POST"
            }
        );

        updateDashboard(data);
    } catch (error) {
        console.error(
            "Simulation Toggle Error:",
            error
        );

        if (modeMessage) {
            modeMessage.textContent =
                "Unable to change heat-spike simulation.";
        }
    } finally {
        toggleSimulationButton.disabled = false;
    }
}


/* =========================================================
   EVENT LISTENERS
========================================================= */

if (fanSlider) {
    fanSlider.addEventListener(
        "input",
        () => {
            isUpdatingFan = true;

            const speed = Number(
                fanSlider.value
            );

            if (fanSpeedValue) {
                fanSpeedValue.textContent =
                    `${speed}%`;
            }

            if (controlSpeedValue) {
                controlSpeedValue.textContent =
                    `${speed}%`;
            }

            if (sliderValue) {
                sliderValue.textContent =
                    `${speed}%`;
            }

            if (chartFanSpeedValue) {
                chartFanSpeedValue.textContent =
                    `${speed}%`;
            }

            if (coolingStateValue) {
                coolingStateValue.textContent =
                    speed > 0
                        ? "Active"
                        : "Stopped";
            }

            updateFanSliderProgress(speed);
            updateFanAnimation(speed);
        }
    );

    fanSlider.addEventListener(
        "change",
        async () => {
            await setFanSpeed(
                fanSlider.value
            );

            isUpdatingFan = false;
        }
    );
}


if (autoModeButton) {
    autoModeButton.addEventListener(
        "click",
        toggleAutoMode
    );
}


if (heatSpikeButton) {
    heatSpikeButton.addEventListener(
        "click",
        triggerHeatSpike
    );
}


if (toggleSimulationButton) {
    toggleSimulationButton.addEventListener(
        "click",
        toggleHeatSimulation
    );
}


/* =========================================================
   START LIVE MONITORING
========================================================= */

initializeChart();

fetchServerStatus();

setInterval(
    fetchServerStatus,
    2000
);