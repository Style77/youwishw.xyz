import os
from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models

from django.contrib.auth.models import User


def upload_path_handler(instance, filename):
    return f"songs/{instance.author.username}/{filename}"


class Song(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    song_id = models.BigIntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=64)
    file = models.FileField(upload_to=upload_path_handler, validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    views = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
