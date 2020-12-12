from .models import GuestSurvey
from surveys.models import Product, Survey

def products_all():
    return Product.objects.all().count()


def survey_users_all():
    return GuestSurvey.objects.all().count()


def surveys_taken_all():
    return Survey.objects.all().count()