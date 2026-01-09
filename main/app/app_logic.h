#pragma once

void app_init(void);

void app_on_mqtt_data(
    const char *topic,
    int topic_len,
    const char *data,
    int data_len
);