from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datacenter.models import Passcard, Visit
from datetime import timedelta

def get_duration(entered_at, leaved_at):
    """Возвращает продолжительность визита в секундах."""
    if leaved_at is None:
        leaved_at = timezone.now()
    duration = leaved_at - entered_at
    return duration

def format_duration(duration):
    """Форматирует продолжительность в строку 'HH:MM:SS'."""
    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{hours:02}:{minutes:02}:{seconds:02}'

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    this_passcard_visits = []
    visits = Visit.objects.filter(passcard=passcard)

    for visit in visits:
        duration = get_duration(visit.entered_at, visit.leaved_at)
        this_passcard_visits.append({
            'entered_at': timezone.localtime(visit.entered_at).strftime('%d-%m-%Y %H:%M'),
            'duration': format_duration(duration),
            'is_strange': duration > timedelta(hours=1),
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

