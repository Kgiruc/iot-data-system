/*
 * SPDX-FileCopyrightText: 2010-2022 Espressif Systems (Shanghai) CO LTD
 *
 * SPDX-License-Identifier: CC0-1.0
 */

#include <stdio.h>
#include <inttypes.h>
#include "sdkconfig.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_chip_info.h"
#include "esp_flash.h"
#include "esp_system.h"
#include "driver/gpio.h"
#include "nvs_flash.h"
#include  "esp_log.h"
#include "wifi_mode.h"
#include "mqtt_broker.h"
#include "app_logic.h"
#include "board/board.h"

void app_main(void)
{
board_init();
 wifi_start_sta();

 vTaskDelay(pdMS_TO_TICKS(3000));
app_init();
 mqtt_publish_test_start();

 

}
