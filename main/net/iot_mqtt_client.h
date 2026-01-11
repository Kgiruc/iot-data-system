#pragma once

typedef void(*iot_mqtt_data_cb_t) (
    const char *topic, 
    int topic_len, 
    const char *data, 
    int data_len);

void iot_mqtt_client_set_data_callback(iot_mqtt_data_cb_t cb);
void iot_mqtt_client_start(void);
void iot_mqtt_client_deliver_data(const char *topic, int topic_len,
                                  const char *data, int data_len);