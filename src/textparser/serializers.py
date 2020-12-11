from rest_framework import serializers
from .models import ParserData


class ParserDataSerializer(serializers.ModelSerializer):
    text = serializers.CharField(read_only=True)
    picture = serializers.ImageField(write_only=True)

    class Meta:
        model = ParserData
        exclude = ['id']
