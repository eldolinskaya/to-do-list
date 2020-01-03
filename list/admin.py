from django.contrib import admin
from .models import List

class ListAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'pk',
        'name',
        'done',
    ]
admin.site.register(List, ListAdmin)