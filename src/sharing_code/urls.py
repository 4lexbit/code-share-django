from django.urls import path
from . import views

urlpatterns = [
    path('create', views.createSnippet, name='create'),
    path('snippet/<uuid:pk>', views.ViewSnippet.as_view(), name='detail'),
]

app_name = 'snippet'
