from PIL import Image
from django.shortcuts import render

# Create your views here.
from pytesseract import pytesseract
from rest_framework import views, status
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.response import Response

from .models import ParserData
from .serializers import ParserDataSerializer


class UploadAndParse(views.APIView):
    """
    Загрузка файла и отправка ответа
    """
    parser_classes = (MultiPartParser, FileUploadParser,)

    def post(self, request):
        file_serializer = ParserDataSerializer(data=request.data)

        if file_serializer.is_valid():

            file = file_serializer.validated_data['picture']
            text = pytesseract.image_to_string(Image.open(file))
            file_serializer.validated_data['text'] = text

            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
