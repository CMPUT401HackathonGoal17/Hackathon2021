from django import forms
from .models import User

class UserForm(forms.ModelForm):
    karma = forms.IntegerField(required=False)
    comrades = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['name', 'karma', 'comrades']
        