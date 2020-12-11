from django.urls import path, include


urlpatterns = [
    path('tesseract/', include('src.textparser.urls')),
]