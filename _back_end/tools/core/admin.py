from django.contrib import admin

from .models import Tools

class ToolsAdmin(admin.ModelAdmin):
    list_display = ('title', 'url',)
    
    pass
    
admin.site.register(Tools, ToolsAdmin)