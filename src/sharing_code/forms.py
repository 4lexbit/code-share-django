from django import forms
from .models import Snippet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, ButtonHolder, Field, Div, HTML


class SnippetForm(forms.ModelForm):
    helper = FormHelper()

    class Meta():
        model = Snippet
        # widgets = {}
        fields = {'title', 'code', 'lang'}
        labels = {
            'title': "Snippet Title",
            'lang': "Choose syntax ",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title', css_class='qwerty'),
            Field('code', css_class=''),
            Div(
                Field('lang', css_class=''),
                HTML(
                    '<div class="form-group g-recaptcha" data-sitekey="6LfzZlAaAAAAANHl7mevl6PaGUzu1S9YquYL77jX"></div>'),
                ButtonHolder(
                    Submit('submit', 'Submit',
                           css_class='border border-indigo-500 bg-indigo-500 text-white rounded-md px-4 py-2 m-2 w-auto transition duration-500 ease select-none hover:bg-indigo-600 focus:outline-none focus:shadow-outline')
                ),
                css_class='grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3 gap-4'
            )
        )
