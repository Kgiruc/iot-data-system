#include "iot_mqtt_client.h"
#include "mqtt_client.h"
#include "esp_event.h"
#include "esp_log.h"


static esp_mqtt_client_handle_t s_client = NULL;
static const char *TAG = "IOT_MQTT";
static iot_mqtt_data_cb_t s_data_cb = 0;
#define MQTT_BROKER_URI "mqtt://192.168.1.26:1883"

void iot_mqtt_client_set_data_callback(iot_mqtt_data_cb_t cb)
{
    
    s_data_cb = cb;
}

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


void iot_mqtt_client_start(void)
{
    (void)s_data_cb;
    
    esp_mqtt_client_config_t cfg = {
        .broker.address.uri = MQTT_BROKER_URI,
        .network.disable_auto_reconnect = false,
    };

    s_client = esp_mqtt_client_init(&cfg);
    esp_mqtt_client_register_event(s_client, ESP_EVENT_ANY_ID, mqtt_event_handler, NULL);
    esp_mqtt_client_start(s_client);
}

void iot_mqtt_client_deliver_data(const char *topic, int topic_len,
                                  const char *data, int data_len)
{
    if (s_data_cb) {
        s_data_cb(topic, topic_len, data, data_len);
       
    }
}