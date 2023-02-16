import pytz
from django.db import models
from django.utils.timezone import localtime, now


class Passcard(models.Model):
    """Object model <Passcard>"""
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'
    

class Visit(models.Model):
    """Object model <Visit>"""
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)
    duration = 0

    def __str__(self):
        """String form of object"""
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        """Calculate duration time"""
        moscow_enter_time = localtime(self.entered_at, pytz.timezone('Europe/Moscow'))
        if self.leaved_at:
            moscow_leave_time = localtime(self.leaved_at, pytz.timezone('Europe/Moscow'))
        else:
            moscow_leave_time = localtime(now(), pytz.timezone('Europe/Moscow'))

        delta = moscow_leave_time - moscow_enter_time
        self.duration = delta.total_seconds()
        return self.duration

    def format_duration(self):
        """Print duration in string format"""
        self.get_duration()
        hours = int(self.duration // 3600)
        minutes = int((self.duration % 3600) // 60)
        return f'{hours}:{minutes}'

    def is_long(self, minutes=60):
        """Determine is visit long or not"""
        return (self.get_duration() > (minutes*60))

