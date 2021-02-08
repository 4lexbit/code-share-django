from django import forms
from .models import Snippet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class SnippetForm(forms.ModelForm):
    helper = FormHelper()

    class Meta():
        model = Snippet
        #widgets = {}
        fields = {'title', 'code', 'lang'}
        labels = {
            'title': "Snippet Title",
            'lang': "Choose syntax ",
        }
