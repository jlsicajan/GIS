from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .forms.event_form import EventForm
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Event


class IndexView(generic.ListView):
    template_name = 'connect7/index.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        """
        Return list of Events
        """
        return Event.objects.order_by('created_at')


class DetailView(generic.DetailView):
    model = Event
    template_name = 'connect7/detail.html'

    def get_queryset(self):
        """
        Return Event.
        """
        return Event.objects


class ResultsView(generic.DetailView):
    model = Event
    template_name = 'connect7/results.html'


def create_event(request):
    return render(request, 'connect7/detail.html')
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'gis/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse('gis:results', args=(question.id,)))


class EventView(FormView):
    template_name = 'connect7/event/event.html'
    form_class = EventForm
    success_url = '../connect7/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)


class EventCreate(CreateView):
    template_name = 'connect7/event/event_form.html'
    form_class = EventForm
    success_url = '../connect7/'


class EventUpdate(UpdateView):
    model = Event
    form_class = EventForm


class EventDelete(DeleteView):
    model = Event
    success_url = '../connect7/'
