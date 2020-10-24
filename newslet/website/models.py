from django.db import models


class TestModel(models.Model):
    title = models.CharField(max_length=100)


class WisdomNote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=120, default='Annonymous')
