from django.forms import ModelForm

from ..models import Event


class BootstrapModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class EventForm(BootstrapModelForm):
    class Meta:
        model = Event
        fields = ['event_date',
                  'begins',
                  'ends',
                  'multi_day_event',
                  'multi_day_ends_date',
                  'repeat',
                  'location',
                  'event_name',
                  'description']
