from django.utils import timezone
from datacenter.models import Visit
from django.shortcuts import render


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


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at__isnull=True)

    visits_data = []
    for visit in non_closed_visits:
        duration = get_duration(visit.entered_at, visit.leaved_at)
        visits_data.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': timezone.localtime(visit.entered_at).strftime('%d-%m-%Y %H:%M'),
            'duration': format_duration(duration),
        })

    context = {
        'non_closed_visits': visits_data,
    }
    return render(request, 'storage_information.html', context)

