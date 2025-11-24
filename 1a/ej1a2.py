"""
Enunciado:
Desarrolla un conjunto de funciones para gestionar eventos en diferentes zonas horarias, facilitando la creación,
manipulación y consulta de eventos programados utilizando Python, con especial énfasis en el manejo de fechas, horas y
zonas horarias mediante datetime y pytz.

Funciones a desarrollar:
- `create_event(name: str, datetime_start: datetime, timezone_str: str) -> Dict[str, str]`:
    Descripción:
    Crea un diccionario representando un evento, incluyendo su nombre, fecha y hora de inicio, y zona horaria.
    Parámetros:
        - `name` (str): Nombre del evento.
        - `datetime_start` (datetime): Fecha y hora de inicio del evento.
        - `timezone_str` (str): Identificador de la zona horaria del evento.

- `time_until_event(event: Dict[str, str]) -> timedelta`:
    Descripción:
    Calcula el tiempo restante hasta el inicio de un evento dado.
    Parámetros:
        - `event` (Dict[str, str]): Evento para calcular el tiempo restante.

- `change_event_timezone(event: Dict[str, str], new_timezone_str: str) -> Dict[str, str]`:
    Descripción:
    Cambia la zona horaria de un evento existente a una nueva especificada.
    Parámetros:
        - `event` (Dict[str, str]): Evento a modificar.
        - `new_timezone_str` (str): Nueva zona horaria.

- `find_next_event(events: List[Dict[str, str]]) -> Optional[Dict[str, str]]`:
    Descripción:
    Identifica el próximo evento entre una lista de eventos, considerando la fecha y hora actual.
    Parámetros:
        - `events` (List[Dict[str, str]]): Lista de eventos entre los cuales buscar el próximo evento.

Ejemplo:
    event1 = create_event("Global Meeting", datetime(2024, 9, 10, 10, 0), "UTC")
    event2 = create_event("Python Talk", datetime(2024, 9, 10, 18, 30), "America/New_York")
    event3 = create_event("Data Science Workshop", datetime(2024, 9, 10, 12, 0), "Europe/London")

Salida esperada:
- Crear eventos con sus respectivas zonas horarias y la consulta del tiempo restante hasta el inicio de cada uno,
demostrando la manipulación y gestión eficaz de eventos en un contexto global.
- La capacidad de cambiar dinámicamente la zona horaria de un evento y calcular cuál será el siguiente evento.
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
import pytz


def create_event(name: str, datetime_start: datetime, timezone_str: str) -> Dict[str, str]:
    timezone = pytz.timezone(timezone_str)
    datetime_with_tz = timezone.localize(datetime_start)
    return {"name": name, "datetime_start": datetime_with_tz, "timezone": timezone_str}


def time_until_event(event: Dict[str, str]) -> timedelta:
    now = datetime.now(pytz.timezone(event["timezone"]))
    difference = event["datetime_start"] - now
    return difference


def change_event_timezone(event: Dict[str, str], new_timezone_str: str) -> Dict[str, str]:
    new_timezone = pytz.timezone(new_timezone_str)
    event["datetime_start"] = event["datetime_start"].astimezone(new_timezone)
    event["timezone"] = new_timezone_str
    return event


def find_next_event(events: List[Dict[str, str]]) -> Optional[Dict[str, str]]:
    now = datetime.now(pytz.utc)
    future_events = [event for event in events if event["datetime_start"] > now]
    if not future_events:
        return None
    next_event = min(future_events, key=lambda event: event["datetime_start"])
    return next_event


# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
    event1 = create_event("Global Meeting", datetime(2024, 9, 10, 10, 0), "UTC")
    event2 = create_event("Python Talk", datetime(2024, 9, 10, 18, 30), "America/New_York")
    event3 = create_event("Data Science Workshop", datetime(2024, 9, 10, 12, 0), "Europe/London")

    for event in [event1, event2, event3]:
        time_to_event = time_until_event(event)
        print(f"Time until '{event['name']}':", time_to_event)

    changed_event1 = change_event_timezone(event1, "America/New_York")
    print(f"Event after timezone change: {changed_event1}")

    events = [event1, event2, event3]
    next_event = find_next_event(events)
    if next_event:
        print("\nThe next event is:", next_event["name"])
    else:
        print("There are no future events.")
