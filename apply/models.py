from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class University(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    acronym = models.CharField(max_length=256)
    logo = models.ImageField(upload_to='logos/')
    uni_type = models.CharField(max_length=256)
    overview = models.TextField(max_length=2000)
    establishedـyear = models.IntegerField()
    students_num = models.IntegerField()
    link = models.CharField(max_length=1000)
    apply_rate = models.CharField(max_length=32)

    def __str__(self):
        return self.name
