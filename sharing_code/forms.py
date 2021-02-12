from django import forms
from .models import Snippet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, ButtonHolder, Field, Div, HTML


class SnippetForm(forms.ModelForm):
    helper = FormHelper()

    class Meta():
        model = Snippet
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Snippet title'}),
            'code': forms.Textarea(attrs={'placeholder': 'Your snippet code'}),
        }
        fields = {'title', 'code', 'lang'}
        labels = {
            'title': '',
            'code': '',
            'lang': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('title', css_class='focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent', ),
                Field('code', css_class='focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent'),
                Field('lang', css_class='focus:ring-2 focus:ring-indigo-500'),
                Div(
                    HTML(
                        '<div class="g-recaptcha" data-sitekey="6LeNDFUaAAAAAFUj-c8ILIrEgIggG87RVg5hATb0"></div>'),
                    Submit('submit', 'Submit', css_class='w-full py-6 border-2 bg-white border-indigo-500 text-indigo-500 font-bold rounded-md transition duration-300 ease-in-out hover:bg-indigo-500  hover:text-white'),
                    css_class='flex items-center buttons'
                )
                ,
                css_class='rounded-3xl mx-auto w-10/12 flex flex-col text-gray-800 border border-gray-300 p-4 shadow-lg max-w-2xl'
            )
        )
