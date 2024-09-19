from django.db import models
from django.core.validators import FileExtensionValidator

class PriceAdvantage(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField('Destination Location', max_length=100)
    description = models.TextField('Destination Description', null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    departure_time = models.DateTimeField()
    return_time = models.DateTimeField()
    dress_code = models.CharField(max_length=255, null=True, blank=True)
    price = models.PositiveIntegerField(default=35000, null=True, blank=True)
    departure_mode = models.CharField(max_length=255, null=True, blank=True)
    duration = models.CharField(max_length=50, null=True, blank=True)
    destination_picture = models.ImageField(upload_to='destination_pics/', null=True, blank=True, validators=[
        FileExtensionValidator(['jpeg', 'jpg'])])
    price_include = models.ManyToManyField(PriceAdvantage, blank=True)

    def __str__(self):
        return self.name
