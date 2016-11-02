from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from notes.models import Categories, Notes
from . import views

urlpatterns = [url(r'^$', views.index, name='index')]


# urlpatterns = [url(r'^$', ListView.as_view(queryset=Notes.objects.all(),
# 	template_name="notes/notes.html"))]