from django import forms
from .models import UserGoal1

class UserG1Form(forms.ModelForm):
    user = forms.ForeignKey(required=False)

    class Meta:
        model = UserGoal1
        fields = ['user']
        