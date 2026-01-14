#include <string.h>
#include "esp_log.h"
#include "mqtt_client.h"
#include "esp_event.h"
#include "driver/gpio.h"
#include "net/iot_mqtt_client.h"

static const char *TAG = "MQTT_TEST";


#define MQTT_BROKER_URI "mqtt://192.168.1.26:1883"


static esp_mqtt_client_handle_t s_client = NULL;

static void mqtt_event_handler(void *handler_args,
                               esp_event_base_t base,
                               int32_t event_id,
                               void *event_data)
{
    esp_mqtt_event_handle_t event = (esp_mqtt_event_handle_t)event_data;
    
    
    
    
    
    if (event_id == MQTT_EVENT_CONNECTED) {
        ESP_LOGI(TAG, "MQTT CONNECTED");

        esp_mqtt_client_subscribe_single(s_client, "iot/light", 0);
                return;
    }

    if (event_id == MQTT_EVENT_DATA) {
        iot_mqtt_client_deliver_data(event->topic, event->topic_len, event->data, event->data_len);
        return;
    }

    if (event_id == MQTT_EVENT_DISCONNECTED) {
        ESP_LOGW(TAG, "MQTT DISCONNECTED");
        return;
    }

    if (event_id == MQTT_EVENT_ERROR) {
        ESP_LOGE(TAG, "MQTT ERROR");
        return;
    }
}

void mqtt_publish_test_start(void)
{
    esp_mqtt_client_config_t cfg = {
        .broker.address.uri = MQTT_BROKER_URI,
        .network.disable_auto_reconnect = false,
    };

    s_client = esp_mqtt_client_init(&cfg);
    esp_mqtt_client_register_event(s_client, ESP_EVENT_ANY_ID, mqtt_event_handler, NULL);
    esp_mqtt_client_start(s_client);

    ESP_LOGI(TAG, "mqtt_publish_test_start: broker=%s ", MQTT_BROKER_URI);
}