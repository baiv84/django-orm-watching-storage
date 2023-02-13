import pytz
from datacenter.models import Visit
from django.utils.timezone import localtime
from django.utils.timezone import now


def get_duration(visit):
    enter_time = visit.entered_at 
    moscow_enter_time = localtime(enter_time, pytz.timezone('Europe/Moscow'))
    moscow_now_datetime = localtime(now(), pytz.timezone('Europe/Moscow'))
    delta = moscow_now_datetime - moscow_enter_time
    return delta.total_seconds()


def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    return f'{hours}:{minutes}'