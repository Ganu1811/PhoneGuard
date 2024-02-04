from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length = 20, unique = True)
    email = models.EmailField(blank = True)

    def __str__(self):
        return self.user.name   


class Contact(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    name = models.CharField(max_length = 250)
    phone_number = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class SpamReport(models.Model):
    reporter = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    reported_number = models.CharField(max_length = 20)

    def __str__(self):
            return self.reporter.user.username