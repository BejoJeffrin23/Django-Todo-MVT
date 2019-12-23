from django import forms
from .models import Todo
#DataFlair
class TodoCreate(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'