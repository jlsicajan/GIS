from django.test import TestCase
from ..forms.event_form import EventForm


class EventFormTest(TestCase):
    def test_forms(self):
        form_data = {
            'event_date': '01/01/1997',
            'begins': '05:00',
            'ends': '06:00',
            'multi_day_event': False,
            'multi_day_ends_date': '',
            'repeat': 'W',
            'location': 'Test',
            'event_name': 'Event Test Name',
            'description': 'Event Test Description',
        }
        form = EventForm(data=form_data)
        self.assertTrue(form.is_valid())
