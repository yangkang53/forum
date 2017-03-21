from django.contrib import admin
from .models import Block


class BlockAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "manager_name", "status")

admin.site.register(Block, BlockAdmin)
