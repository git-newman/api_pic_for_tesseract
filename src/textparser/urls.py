from django.urls import path
from . import views

urlpatterns = [
    path('', views.UploadAndParse.as_view()),
]