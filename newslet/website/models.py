from django.db import models

class Formularz(models.Model):
    imie = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.imie



class TestModel(models.Model):
    title = models.CharField(max_length=100)


class WisdomNote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=120, default='Annonymous')


class NewsTags(models.Model):
    tag_name = models.CharField(max_length=120)

    def __str__(self):
        return self.tag_name

        
class NewsCategory(models.Model):
    category_one = models.CharField(max_length=120, default='Miscellaneous')
    assigned_tag = models.ForeignKey(NewsTags, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.category_one
