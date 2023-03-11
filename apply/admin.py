from django.contrib import admin
from .models import Country, City, University

class CountryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Country, CountryAdmin)


class CityAdmin(admin.ModelAdmin):
    pass
admin.site.register(City, CityAdmin)


class UniversityAdmin(admin.ModelAdmin):
    pass
admin.site.register(University, UniversityAdmin)
