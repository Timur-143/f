from django.db import models

class Coc(models.Model):
    name = models.CharField(max_length=20)
    pas = models.IntegerField(max_length=20)
    mail = models.EmailField()


def __str__(self):
    return self.name