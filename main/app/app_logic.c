#include "app_logic.h"
#include "board.h"
#include "iot_mqtt_client.h"

void app_init(void)
{
    // TODO: tu później zepniemy callback i wystartujemy MQTT
}

void app_on_mqtt_data(const char *topic, int topic_len, const char *data, int data_len)
{
    (void)topic;
    (void)topic_len;
    (void)data;
    (void)data_len;

    // TODO: tu później będzie logika '1'/'0' -> board_led_set(...)
}
