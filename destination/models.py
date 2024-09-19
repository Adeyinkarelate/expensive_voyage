from django.db import models
from django.core.validators import FileExtensionValidator

# Destination


class Destination(models.Model):
    price_advantage = (
        ('Accommondatio', 'Accommondatio'),
        ('Porter & Personal Guide','Porter & Personal Guide'),
        (' Insurance',' Insurance'),
        ('Breakfast','Breakfast'),
        (' Tranportation / Car',' Tranportation / Car')
    )
    
    name = models.CharField('Destination Loction',max_length=100)
    description = models.TextField('Destination Description',null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)
    departure_time = models.DateTimeField()
    return_time = models.DateTimeField()
    dress_code = models.CharField(max_length=255, null=True, blank=True)
    price = models.PositiveIntegerField(default=35000, null=True, blank=True)
    departure_mode = models.CharField(max_length=255, null=True, blank=True)
    duration = models.CharField(max_length=50 , null=True, blank=True)
    destination_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True, validators=[
        FileExtensionValidator(['jpeg', 'jpg'])])
    price_include = models.CharField(max_length=10, choices=price_advantage, null=True, blank=True)

    def __str__(self):
        return self.name
