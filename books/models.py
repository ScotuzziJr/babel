from distutils.command.upload import upload
from platform import release
from pyexpat import model
from statistics import mode
from django.db import models
from uuid import uuid4

def uploadBookCover(instance, fileName):
    return f'{instance.bookID}-{fileName}'

class Books(models.Model):
    bookID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    categorie = models.CharField(max_length=255, default='', blank=True, null=True)
    release_date = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    company = models.CharField(max_length=255)
    createAt = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=uploadBookCover, blank=True, null=True)
