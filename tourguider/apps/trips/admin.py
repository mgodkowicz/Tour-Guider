from django.contrib import admin

from .models import Trip


class TripsAdmin(admin.ModelAdmin):
    readonly_fields = ('duration', 'cost', 'rate')

    class Meta:
        model = Trip

# Register your models here.
admin.site.register(Trip, TripsAdmin)
