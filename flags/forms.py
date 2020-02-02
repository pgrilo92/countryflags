from django.forms import ModelForm
from .models import President, Language

class PresidentForm(ModelForm):
    class Meta: 
        model = President
        fields = ['name', 'start_date', 'end_date']

class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ['language']