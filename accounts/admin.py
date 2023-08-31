from django.contrib import admin
from .models import Detail


@admin.register(Detail)
class DetailsAdmin(admin.ModelAdmin):
    list_display = (
        'species',
    )
