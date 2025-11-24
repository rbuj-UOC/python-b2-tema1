from datetime import datetime, timedelta
import pytest
import pytz
from ej1a2 import create_event, time_until_event, change_event_timezone, find_next_event  


def test_create_event():
    name = "Test Event"
    datetime_start = datetime(2023, 1, 1, 12, 0)  
    timezone_str = "UTC"
    event = create_event(name, datetime_start, timezone_str)
    assert event["name"] == name, "Event name should match the input."
    assert event["timezone"] == timezone_str, "Event timezone should match the input."
    expected_datetime = pytz.timezone(timezone_str).localize(datetime_start)
    assert event["datetime_start"] == expected_datetime, "Event datetime should match the localized input."

def test_time_until_event():
    future_date = datetime.now() + timedelta(days=1)  
    event = create_event("Future Event", future_date, "UTC")
    assert time_until_event(event) > timedelta(), "The event should be in the future."

def test_change_event_timezone():
    event = create_event("Test Event", datetime(2023, 1, 1, 12, 0), "UTC")  
    changed_event = change_event_timezone(event, "America/New_York")
    assert changed_event["timezone"] == "America/New_York", "The timezone should be updated to 'America/New_York'."

def test_find_next_event():
    event1 = create_event("Past Event", datetime.now() - timedelta(days=1), "UTC")  
    future_date = datetime.now() + timedelta(days=1)  
    event2 = create_event("Future Event", future_date, "UTC")
    next_event = find_next_event([event1, event2])
    assert next_event is not None and next_event["name"] == "Future Event", "The next event should be 'Future Event'."
