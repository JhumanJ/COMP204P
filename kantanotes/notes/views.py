from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Categories, Notes, Links 
from django.http import HttpResponse
# Create your views here.

def index(request):
    categorieslist = Categories.objects.all()
    noteslist = Notes.objects.all()
    context = {'categorieslist': categorieslist,'noteslist':noteslist}
    return render(request, 'notes/notes.html', context)

def displayNotes(request, Categories_Id):
    categorieslist = Categories.objects.all()
    category = get_object_or_404(Categories, pk = Categories_Id)
    try:
        noteslist = get_list_or_404(Notes, categoryId = Categories_Id)
        context = {'categorieslist': categorieslist,'noteslist':noteslist}
        return render(request, 'notes/notes.html', context)

    except Notes.DoesNotExist:
        context = {'categorieslist': categorieslist,'errorMessage':"No notes in this category."}
        return render(request, 'notes/notes.html', context)


def deleteCategory(request, Categories_Id):
    categorieslist = Categories.objects.all()
    category = get_object_or_404(Categories, pk = Categories_Id)
    category.delete()
    return redirect('notes:index')
