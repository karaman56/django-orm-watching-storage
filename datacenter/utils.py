from datetime import timedelta
from django.utils import timezone


SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60
LONG_VISIT_THRESHOLD = timedelta(hours=1)

def get_duration(entered_at, leaved_at):
    """Возвращает продолжительность визита в секундах."""
    if leaved_at is None:
        leaved_at = timezone.now()
    duration = leaved_at - entered_at
    return duration

def format_duration(duration):
    """Форматирует продолжительность в строку 'HH:MM:SS'."""
    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, SECONDS_IN_HOUR)
    minutes, seconds = divmod(remainder, SECONDS_IN_MINUTE)
    return f'{hours:02}:{minutes:02}:{seconds:02}'

def is_visit_long(duration):
    """Проверяет, является ли визит долгим."""
    return duration > LONG_VISIT_THRESHOLD

