from django.urls import path
from . import views

urlpatterns = [
    path('', views.SnippetAPIView.as_view()),
    path('snippet/<uuid:pk>', views.SnippetAPIView.as_view())
]