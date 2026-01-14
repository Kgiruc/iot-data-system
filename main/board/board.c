#include "board.h"
#include "driver/gpio.h"

#define LED_GPIO GPIO_NUM_3

void board_init(void)
{
    gpio_set_direction(LED_GPIO, GPIO_MODE_OUTPUT);
}

void board_led_set(bool on)
{
    if(on == true) {
        gpio_set_level(LED_GPIO, 1);
        printf("light");
    } else {
        gpio_set_level(LED_GPIO, 0);
    };
}
