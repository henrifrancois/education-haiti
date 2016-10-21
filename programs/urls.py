from django.conf.urls import url, include
from datetime import datetime

from . import views

urlpatterns = [
    url(r'^$', views.programs, name='programs'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^add_program$', views.add_program, name='add_program'),
]
