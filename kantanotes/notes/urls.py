from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from notes.models import Categories, Notes
from . import views

app_name = 'notes'
urlpatterns = [url(r'^$', views.index, name='index'),
				url(r'^(?P<Categories_Id>[0-9]+)/displayNotes/$', views.displayNotes, name='displayNotes'),
				url(r'^(?P<Categories_Id>[0-9]+)/delete/$', views.deleteCategory, name='deleteCategory'),
			   url(r'^create/', views.addCategory, name='addCategory')]




# urlpatterns = [url(r'^$', ListView.as_view(queryset=Notes.objects.all(),
# 	template_name="notes/notes.html"))]