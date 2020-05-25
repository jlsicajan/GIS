from django.test import TestCase
from ..forms.event_form import EventForm
from datetime import datetime, timedelta, date
from dateutil import parser


class EventFormTest(TestCase):

    def date_validation(self, date_text):
        is_valid = False
        try:
            parser.parse(date_text)
            is_valid = True
        except ValueError:
            pass

        return is_valid

    def test_forms(self):
        time_in_future = datetime.now() + timedelta(hours=4)
        form_data = {
            'event_date': date.today() + timedelta(days=1),
            'begins': datetime.now().strftime("%H:%M:%S"),
            'ends': time_in_future.strftime("%H:%M:%S"),
            'multi_day_event': False,
            'multi_day_ends_date': '',
            'repeat': 'W',
            'location': 'Test',
            'event_name': 'Event Test Name',
            'description': 'Event Test Description',
        }

        event_form = EventForm(data=form_data)

        if form_data['multi_day_event']:
            self.assertTrue(expr=self.date_validation(date_text=form_data['multi_day_ends_date']),
                            msg='End Date value for Multi Day Event is not valid.')
            self.assertLess(a=form_data['event_date'], b=form_data['multi_day_ends_date'],
                            msg='End date should be less than Start date')
            self.assertEqual(first=len(form_data['repeat']), second=0,
                             msg='Repeat is not allowed when if it is a multi day event.')
        else:
            self.assertEqual(first=len(form_data['multi_day_ends_date']), second=0,
                             msg='End date should be empty since it is not a multi day event')
            self.assertLess(a=form_data['begins'], b=form_data['ends'], msg='End time should be higher than begin time.')

        self.assertTrue(expr=event_form.is_valid(), msg=event_form.errors.get_json_data(escape_html=False))
