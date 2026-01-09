#include "iot_mqtt_client.h"

static iot_mqtt_data_cb_t s_data_cb = 0;

void iot_mqtt_client_set_data_callback(iot_mqtt_data_cb_t cb)
{
    s_data_cb = cb;
}

void iot_mqtt_client_start(void)
{
    (void)s_data_cb;
    // TODO: później tu przeniesiemy właściwy kod MQTT z legacy
}