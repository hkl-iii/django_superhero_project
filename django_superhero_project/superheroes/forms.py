from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import  *


class EditSuperHeroForm(ModelForm):
    class Meta:
        model = Superhero
        fields =  '__all__'
        widgets = {
            'release_date': forms.DateInput(attrs={"class":"form-control bg-gray", "type": "date"}),

        }