from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home,name='home'),
     path('notes', views.notes,name='notes'),
     path('delete_note/<int:pk>', views.delete_note, name='delete-note'),
     path('notes_detail/<int:pk>',
         views.NotesDetailView.as_view(), name="notes_detail"),
    path('homework', views.homework, name='homework'),
    path('delete_homework/<int:pk>', views.delete_homework, name='delete-homework'),
    path('update_homework/<int:pk>', views.update_homework, name='update-homework'),
    path('youtube', views.youtube, name='youtube'),
    path('todo', views.todo, name='todo'),
    path('delete_todo/<int:pk>', views.delete_todo, name='delete-todo'),
    path('update_todo/<int:pk>', views.update_todo, name='update-todo'),
    path('books', views.books, name='books'),
    path('wiki', views.wiki, name='wiki'),
    path('dictionary', views.dictionary, name='dictionary'),
]