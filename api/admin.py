from django.contrib import admin
from .models import Site, StatusVals, Pivot

# Register your models here.

admin.site.register(Site)

@admin.register(Pivot)
class PivotAdmin(admin.ModelAdmin):
    list_display = ("status", 'site', 'updated_at')



admin.site.register(StatusVals)
