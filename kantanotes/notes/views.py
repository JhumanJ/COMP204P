from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Categories, Notes, Links 
from django.http import HttpResponse
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
# Create your views here.

class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = ['categoryName', 'description']

@login_required(login_url='/login/')
def index(request):
    categorieslist = Categories.objects.all()
    noteslist = Notes.objects.all()
    context = {'categorieslist': categorieslist,'noteslist':noteslist}
    return render(request, 'notes/notes.html', context)

@login_required(login_url='/login/')
def displayNotes(request, Categories_Id):
    categorieslist = Categories.objects.all()
    category = get_object_or_404(Categories, pk = Categories_Id)

    try:
        noteslist = get_list_or_404(Notes, categoryId = Categories_Id)
        context = {'categorieslist': categorieslist,'noteslist':noteslist}
        return render(request, 'notes/notes.html', context)

    except:
        context = {'categorieslist': categorieslist, 'errorMessage':"No notes in this category."}
        return render(request, 'notes/notes.html', context)

@login_required(login_url='/login/')
def deleteCategory(request, Categories_Id):
    categorieslist = Categories.objects.all()
    category = get_object_or_404(Categories, pk = Categories_Id)
    category.delete()
    return redirect('notes:index')

@login_required(login_url='/login/')
def addCategory(request):
    form = CategoryForm(request.POST or None)
    categorieslist = Categories.objects.all()
    if form.is_valid():
        category = Categories(categoryName = form.cleaned_data['categoryName'],description = form.cleaned_data['description'], userId = request.user)
        category.save()
        return redirect('notes:index')
    return render(request, 'notes/newcat.html', {'form': form,'categorieslist': categorieslist})

