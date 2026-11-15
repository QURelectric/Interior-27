# Interior-27

### Project Structure

- `state.py` – contains the shared vehicle state dictionary (vehicle_state) and a thread lock.
- `canbus.py` – receives and parses CAN messages from the vehicle network, updating vehicle_state with decoded data.
- `can_sim.ino` – Arduino-based CAN simulator used to generate CAN messages.

---

## Installation Guide

1. Clone the repository:
`git clone <repository-url>`
`cd <repository-directory>`
2. Create a Python virtual environment:
`python3 -m venv .venv`
3. Activate the virtual environment:
- On Linux/macOS:
`source .venv/bin/activate`
- On Windows (PowerShell):
`.venv\Scripts\Activate.ps1`
4. Install required packages:
`pip install -r requirements.txt`
