from django import forms
from .models import *


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ('image', )


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('name', 'lvl')
        
    def clean(self):
        clean_data = super().clean()
        name = cleaned_data.get('name')


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('name', 'description', 'story', 'photo', 'skills')
    
    