from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title"]
        labels = {"title": "Todo"}      # field label in the form

