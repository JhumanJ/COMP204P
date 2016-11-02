from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from notes.models import Categories

urlpatterns = [url(r'^$', ListView.as_view(queryset=Categories.objects.all(),
	template_name="notes/home.html"))]