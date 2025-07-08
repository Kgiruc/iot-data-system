from backend.mqtt_client.subscriber import run_subscriber
from backend.modules.temperature.handler import handle_temperature_message

if __name__ == "__main__":
    run_subscriber(handle_temperature_message)
