from django.contrib import admin

from .models import Place, Guide, OpeningHour
# Register your models here.


class PlaceAdmin(admin.ModelAdmin):
    readonly_fields = ('rate', 'is_open')

    class Meta:
        model = Place

# Register your models here.
admin.site.register(Place, PlaceAdmin)
admin.site.register(Guide)
admin.site.register(OpeningHour)
