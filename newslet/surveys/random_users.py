from django.contrib.auth.models import User
from website.models import GuestSurvey
import random


def random_users_emails_list():
    winners = []
    if len(GuestSurvey.objects.all()) < 3:
        return None
        return
    else:
        while True:
            user = GuestSurvey.objects.all().values('quest_email')[random.randint(1, len(GuestSurvey.objects.all()))-1]['quest_email']
            if user in winners:
                continue
            elif len(winners) >= 3:
                if len(winners) >= 3:
                    return winners
                elif user in winners:
                    continue
                else:
                    winners.append(user)


def random_user_email():
    users_list = User.objects.all()
    return GuestSurvey.objects.filter(id=random.randint(1, len(users_list))).values('quest_email')[0]['quest_email']

