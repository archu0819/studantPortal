from django.shortcuts import render, redirect
from .forms import *

import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic

from myApp.models import Notes

# Create your views here.
def home(request):
    return render(request, 'myApp/home.html')

def notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(
                user=request.user, title=request.POST['title'], description=request.POST['description'])
            notes.save()
            messages.success(
                request, f'Notes Added from {request.user.username}!')
    else:
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)

    context = {'form': form, 'notes': notes}
    return render(request, 'myApp/notes.html', context)

class NotesDetailView(generic.DetailView):
    model = Notes

def delete_note(request, pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect('notes')


def homework(request):
   
           
    homeworks = Homework.objects.filter(user=request.user)
    context = {'homeworks': homeworks}
    return render(request, 'myApp/homework.html',context)
   

   