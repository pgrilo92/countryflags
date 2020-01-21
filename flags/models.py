from django.db import models

class Flag(models.Model):
    country = models.CharField(max_length=100)
    capital_city = models.CharField(max_length=100)
    flag_img = models.URLField()
    continent = models.CharField(max_length=100)
    population = models.IntegerField()
    description = models.TextField(max_length=300)

    def __str_(self):
        return self.country

