from django.db import models
from django.contrib.auth.models import User
from surveys.models import Company


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user_company = models.ForeignKey(Company ,on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f'{self.user.username} Profile'


