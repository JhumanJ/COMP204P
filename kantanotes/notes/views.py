from django.shortcuts import render
from .models import Categories, Notes, Links 
from django.http import HttpResponse
# Create your views here.

def index(request):
    categorieslist = Categories.objects.all()
    noteslist = Notes.objects.all()
    context = {'categorieslist': categorieslist,'noteslist':noteslist}
    return render(request, 'notes/categories.html', context)