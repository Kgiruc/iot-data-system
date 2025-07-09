from backend.mqtt_client.subscriber import run_subscriber
from backend.services.mqtt_dispatcher import dispatch

if __name__ == "__main__":
    run_subscriber(dispatch)
