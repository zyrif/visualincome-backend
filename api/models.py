from django.db import models


class Income(models.Model):
    name = models.CharField(max_length=2048)
    init_amount = models.IntegerField()
    final_amount = models.IntegerField()
    start_age = models.IntegerField()
    end_age = models.IntegerField()
