idf_component_register(
    SRCS
        "mqtt_broker.c"
        "wifi_mode.c"
        "hello_world_main.c"
        "app/app_logic.c"
        "board/board.c"
        "net/iot_mqtt_client.c"
    INCLUDE_DIRS
        "app"
        "board"
        "net"
)

