## IoT Data System – Backend
Modularny backend do systemu IoT oparty na MQTT i bazie danych MariaDB. Obsługuje odbieranie, walidację i zapis danych z czujników.

Technologia
Python 3.13

Docker / Docker Compose

MQTT (broker: Mosquitto)

MariaDB (baza danych)

Pytest (testy jednostkowe + end-to-end)

## Struktura projektu
iot-data-system/
├── backend/
│   ├── db/                    # Połączenia z bazą danych
│   ├── modules/common/        # Parsowanie, insert, handler
│   ├── services/              # Dispatcher MQTT
│   ├── validators/            # Walidacja danych
│   ├── schemas/               # Schematy danych
│   ├── utils/                 # Logger i inne
│   ├── config/                # Pliki konfiguracyjne
│   └── main.py                # Punkt startowy aplikacji
├── tests/                     # Testy jednostkowe i e2e
└── docker-compose.yml         # Uruchamianie backendu (produkcyjnie)


## 🚀 Uruchomienie

🔹 Lokalnie (bez Dockera)

1. Stwórz .env i mqtt_topics.env w folderze backend/
2. Uruchom backend:
                    cd backend
                    python main.py

🔹 Produkcyjnie (Docker)

1. Zbuduj obraz:
                docker compose build

2. Uruchom kontener:
                docker compose up -d





## ✅ Uruchamianie testów

Windows (wystarczy kliknąć lub uruchomić z terminala):

> run_tests.bat

Nie wymaga żadnej konfiguracji ani ustawień.  
Testy działają automatycznie z poprawnym `PYTHONPATH`.

