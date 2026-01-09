#pragma once

typedef void(*mqtt_data_cb_t) (
    const char *topic, 
    int topic_len, 
    const char *data, 
    int data_len);

void mqtt_client_set_data_callback(mqtt_data_cb_t cb);
void mqtt_client_start(void);