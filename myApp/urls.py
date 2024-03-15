from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home,name='home'),
     path('notes', views.notes,name='notes'),
     path('delete_note/<int:pk>', views.delete_note, name='delete-note'),
]