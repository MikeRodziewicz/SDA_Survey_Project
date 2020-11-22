from django.db import models


class GuestSurvey(models.Model):
    guest_name = models.CharField(max_length=120)
    quest_email = models.EmailField(max_length=254)
