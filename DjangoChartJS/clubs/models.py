from django.db import models

class Club(models.Model):
    name = models.CharField(),
    money = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.name, self.money)