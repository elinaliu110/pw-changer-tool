# pw-changer-tool

A lightweight Python-based GUI utility designed to batch update user passwords via REST API. This tool is built with **Tkinter** for the interface and **Requests** for API communication.

## Key Features
* **Graphical User Interface**: Easy-to-use input fields, no command-line knowledge required.
* **Batch Processing**: Supports updating multiple emails at once (comma-separated).
* **Security**: Supports Bearer Token authentication for privacy.
* **Instant Feedback**: Displays a detailed success/failure report in a popup window after execution.

## Project Structure
```bash
ModbusSimulator/
│
├── MODBUS_TCP_Server_v22_IoTEdge.py    # Main Python script
├── Dockerfile                          # Docker configuration
├── deployment.yaml                     # Kubernetes deployment config
├── service.yaml                        # Kubernetes service config
└── README.md                           # Document
```

## Getting Started

### 1. Prerequisites
* Python 3.x
* modbus-tk
* numpy

### 2. Local Setup
