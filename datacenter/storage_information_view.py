from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    """Print non closed visits"""
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
        owner_name = visit.passcard.owner_name
        one_visit = dict(who_entered=owner_name, entered_at=visit.entered_at, \
                         duration=visit.get_duration(), format_duration=visit.format_duration())
        non_closed_visits.append(one_visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
