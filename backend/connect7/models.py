from django.db import models


class Event(models.Model):
    REPEAT_CHOICES = (
        ('N', 'Never'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('Y', 'Yearly'),
    )

    event_id = models.AutoField(primary_key=True, db_column='event_id')
    event_date = models.DateField(db_column='event_date')
    begins = models.TimeField(db_column='begins')
    ends = models.TimeField(db_column='ends')

    multi_day_event = models.BooleanField(db_column='multi_day_event', default=0)
    multi_day_ends_date = models.DateField(null=True, blank=True, db_column='multi_day_ends_date')
    repeat = models.CharField(max_length=1, choices=REPEAT_CHOICES, db_column='repeat')
    location = models.CharField(max_length=180, db_column='location')

    event_name = models.CharField(max_length=180, db_column='event_name')
    description = models.TextField(max_length=900, db_column='description')

    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at')
    updated_at = models.DateTimeField(auto_now=True, db_column='updated_at')

    class Meta:
        db_table = u'Event'

    def __unicode__(self):
        return self.event_name
