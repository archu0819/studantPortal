from django.shortcuts import render, redirect
from .forms import *

import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic

from myApp.models import Notes
from youtubesearchpython import VideosSearch

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
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            homeworks = Homework(
                user=request.user, subject=request.POST['subject'], title=request.POST['title'], description=request.POST['description'], due=request.POST['due'], is_finished=finished)
            homeworks.save()
            messages.success(
                request, f'Homework Added from {request.user.username}!')
    else:
        form = HomeworkForm()
    homeworks = Homework.objects.filter(user=request.user)
    if len(homeworks) == 0:
        homeworks_done = True
    else:
        homeworks_done = False
    homeworks = zip(homeworks, range(1, len(homeworks)+1))
    context = {'form': form, 'homeworks': homeworks,
               'homeworks_done': homeworks_done}
    return render(request, 'myApp/homework.html', context)


def youtube(request):
    if request.method == "POST":
        form = DashboardForm(request.POST)
        text = request.POST['text']
        videos = VideosSearch(text, limit=5)
        result_list = []
        print(videos.result())
        for i in videos.result()['result']:
            result_dict = {
                'input': text,
                'title': i['title'],
                'duration': i['duration'],
                'thumbnail': i['thumbnails'][0]['url'],
                'channel': i['channel']['name'],
                'link': i['link'],
                'views': i['viewCount']['short'],
                'published': i['publishedTime'],
            }
            desc = ''

            for j in i['descriptionSnippet']:
                desc += j['text']
            result_dict['description'] = desc
            result_list.append(result_dict)
        return render(request, 'myApp/youtube.html', {'form': form, 'results': result_list})
    else:
        form = DashboardForm()
    return render(request, 'myApp/youtube.html', {'form': form})


def delete_homework(request, pk=None):
    Homework.objects.get(id=pk).delete()
    if 'profile' in request.META['HTTP_REFERER']:
        return redirect('profile')
    return redirect('homework')


def update_homework(request, pk=None):
    homework = Homework.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    if 'profile' in request.META['HTTP_REFERER']:
        return redirect('profile')
    return redirect('homework')
   

   