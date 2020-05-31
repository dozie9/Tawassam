from django import forms
from .models import Set

#DataFlair
class SetCreate(forms.ModelForm):
    class Meta:
        model = Set
        exclude = ('author',)
