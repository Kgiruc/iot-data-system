#include "iot_mqtt_client.h"
#include <stdio.h>

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

void iot_mqtt_client_deliver_data(const char *topic, int topic_len,
                                  const char *data, int data_len)
{
    if (s_data_cb) {
        s_data_cb(topic, topic_len, data, data_len);
       
    }
}