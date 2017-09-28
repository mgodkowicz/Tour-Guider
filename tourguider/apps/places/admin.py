from django.contrib import admin

from .models import Place, Guide, OpeningHour
# Register your models here.


admin.site.register(Place)
admin.site.register(Guide)
admin.site.register(OpeningHour)
