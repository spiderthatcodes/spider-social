from django.contrib import admin
from .models import Detail


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = (
        'species',
    )
