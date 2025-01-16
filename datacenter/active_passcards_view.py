from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def active_passcards_view(request):

    passcards = Passcard.objects.all()

    active_passcards = passcards.filter(is_active=True)

    active_passcards_count = active_passcards.count()

    context = {
        'active_passcards': active_passcards,
        'active_passcards_count': active_passcards_count,
    }

    return render(request, 'active_passcards.html', context)
