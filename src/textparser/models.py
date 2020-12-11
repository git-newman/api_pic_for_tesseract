from django.db import models

# Create your models here.


class ParserData(models.Model):
    picture = models.ImageField(upload_to='user/tesseract/',
                                blank=False,
                                null=False)
    text = models.TextField(blank=True, null=True)
