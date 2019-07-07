from django import forms
from .models import Shoppinglist


class NameForm(forms.ModelForm):
    class Meta:
        model = Shoppinglist
        fields = ('title', 'description', 'price')
