from datetime import timedelta  # Добавьте этот импорт
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datacenter.models import Passcard, Visit
from datacenter.utils import get_duration, format_duration

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

