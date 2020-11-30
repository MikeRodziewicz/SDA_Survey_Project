from django.contrib.auth.models import User
from website.models import GuestSurvey
import random


def random_users_emails_list():
    winners = []
    users_list = GuestSurvey.objects.all()
    while True:
        user = GuestSurvey.objects.filter(id=random.randint(1, len(users_list))).values('quest_email')[0]['quest_email']
        if user in winners:
            continue
        elif len(winners) == 3:
            return winners
        else:
            winners.append(user)


def random_user_email():
    users_list = User.objects.all()
    return GuestSurvey.objects.filter(id=random.randint(1, len(users_list))).values('quest_email')[0]['quest_email']

