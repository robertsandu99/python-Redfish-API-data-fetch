# Redfish API Simulation

This project simulates a Redfish API for retrieving hardware data using Python.

The app is using endpoints to mimic a server's Redfish interface and simulate data for:

- Power usage
- CPU temperature
- Memory temperature
- Fan speed

Each endpoint reads from local JSON files and returns the corresponding data.

How to run:

- install python 3.11+ on your machine
- in a terminal use: `pip install poetry`
- cd into the app directory - you should pyproject.toml in the directory.
- in terminal use: `poetry install`
- in terminal use: `poetry shell`
- to run the server (Redfish API simulation): `poetry run uvicorn app:app --reload`
- do not close the current termina, but open another one.
- in the new terminal run the app.py (`py app.py`, `python app.py`, `python3 app.py`, or just run it from IDE)
- follow the instruction from terminal
