from django.contrib import admin
from .models import *


class MacroeconomicsAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id",)
    
    # search_fields = ("name", "description")
    # list_editable = ("name", "description")
    # list_filter = ("name", "description")


admin.site.register(Topic, MacroeconomicsAdmin)
admin.site.register(Economic_index)
admin.site.register(Table)
