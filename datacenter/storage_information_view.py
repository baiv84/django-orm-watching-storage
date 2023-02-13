from basic.timefuncs import get_duration
from basic.timefuncs import format_duration
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    not_leaved_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in not_leaved_visits:
        owner_name = visit.passcard.owner_name
        entered_at = visit.entered_at
        duration = get_duration(visit)
        print_duration = format_duration(duration)
        one_visit = dict(who_entered=owner_name, entered_at=entered_at, duration=print_duration)    
        non_closed_visits.append(one_visit)
        
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
