from django.contrib import admin
from .models import Destination , PriceAdvantage
# Register your models here.

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    pass


admin.site.register(PriceAdvantage)