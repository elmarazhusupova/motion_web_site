from django.db import models


class ClubConsulting(models.Model):
    username = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)

    def __str__(self):
        return self.username


# class PracticeLesson(models.Model):
#     username = models.CharField(max_length=250)
#     phone_number = models.CharField(max_length=250)
