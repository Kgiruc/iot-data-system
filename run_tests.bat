@echo off
cd /d %~dp0iot-data-system
set PYTHONPATH=backend
pytest -v