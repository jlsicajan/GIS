from django.urls import path

from . import views

app_name = 'connect7'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('details/event/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('/store/', views.create_event, name='create_event'),

    path('event/add/', views.EventCreate.as_view(), name='event-add'),
    path('event/<int:pk>/', views.UpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', views.EventDelete.as_view(), name='event-delete'),
]

