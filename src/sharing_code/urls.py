from django.urls import path
from . import views
from .decorators import check_recaptcha

urlpatterns = [
    path('create', check_recaptcha(views.CreateSnippet.as_view()), name='create'),
    path('snippet/<uuid:pk>', views.ViewSnippet.as_view(), name='detail'),
]

app_name = 'snippet'
