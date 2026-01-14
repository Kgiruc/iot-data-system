#include <stdio.h>
#include <string.h>
#include "app_logic.h"
#include "board.h"
#include "iot_mqtt_client.h"

#define LIGHT_TOPIC "iot/light"

void app_init(void)
{
    iot_mqtt_client_set_data_callback(app_on_mqtt_data);
    // iot_mqtt_client_start();
}

void app_on_mqtt_data(const char *topic, int topic_len, const char *data, int data_len)
{
      if (data_len <= 0) {
        return;
    }

    const int expected_len = (int)strlen(LIGHT_TOPIC);
    if (topic_len != expected_len) {
        return;
    }

    if (memcmp(topic, LIGHT_TOPIC, (size_t)topic_len) != 0) {
        return;
    }

    if (data[0] == '1') {
        board_led_set(true);
    } else if (data[0] == '0') {
        board_led_set(false);
    }
}
