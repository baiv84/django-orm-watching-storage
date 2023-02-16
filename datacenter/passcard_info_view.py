from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    """Print visits per one passcard"""
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    for visit in visits:
        one_passcard_visit = dict(entered_at=visit.entered_at, duration=visit.get_duration(), \
                                  format_duration=visit.format_duration(), is_strange=visit.is_long(60))
        this_passcard_visits.append(one_passcard_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
