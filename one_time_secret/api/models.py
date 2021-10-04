from django.db import models


# Create your models here.
class Secret(models.Model):
    text = models.TextField(verbose_name='Текст секрета')
    password = models.CharField(max_length=100, verbose_name='Кодовое слово')
