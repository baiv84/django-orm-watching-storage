from django.db import models
from django.utils.timezone import localtime


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

    def __str__(self):
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
        storage_enter_time = localtime(self.entered_at)
        if self.leaved_at:
            storage_leave_time = localtime(self.leaved_at)
        else:
            storage_leave_time = localtime()
        delta = storage_leave_time - storage_enter_time
        return delta.total_seconds()

    def format_duration(self):
        """Print duration time in string format"""
        duration_time = self.get_duration() 
        hours = int(duration_time // 3600)
        minutes = int((duration_time % 3600) // 60)
        return f'{hours}:{minutes}'

    def is_long(self, minutes=60):
        """Determine is visit long or not"""
        return (self.get_duration() > (minutes*60))
