from django.utils import timezone
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.utils import get_duration, format_duration, is_visit_long  # Импортируем новую функцию

def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at__isnull=True)

    visits_data = []
    for visit in non_closed_visits:
        duration = get_duration(visit.entered_at, visit.leaved_at)
        visits_data.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': timezone.localtime(visit.entered_at).strftime('%d-%m-%Y %H:%M'),
            'duration': format_duration(duration),
            'is_strange': is_visit_long(duration),
        })

    context = {
        'non_closed_visits': visits_data,
    }
    return render(request, 'storage_information.html', context)


