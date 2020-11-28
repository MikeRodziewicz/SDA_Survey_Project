from django.contrib.auth.models import User
import random


def random_users_emails_list():
    winners = []
    users_list = User.objects.all()
    while True:
        user = User.objects.filter(id=random.randint(1, len(users_list))).values('email')[0]['email']
        if user in winners:
            continue
        elif len(winners) == 3:
            return winners
        else:
            winners.append(user)


def random_user_email():
    users_list = User.objects.all()
    return User.objects.filter(id=random.randint(1, len(users_list))).values('email')[0]['email']

