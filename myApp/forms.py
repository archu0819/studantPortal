from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']