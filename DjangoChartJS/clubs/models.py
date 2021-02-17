from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=60, default='London')
    city = models.CharField(max_length=60, default='London')
    money = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.city} {self.money}"