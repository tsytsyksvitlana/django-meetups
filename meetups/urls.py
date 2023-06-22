from django.urls import path

from . import views

urlpatterns=[
    path('meetups/', views.index),
    path('meetups/<slug:meetup_slug>', views.metup_details)
]