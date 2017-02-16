from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('proj_name', 'user', 'proj_file', 'upload_date', 'expire_date')
    fieldsets = [
        ('User', {'fields': ['user']}),
        ('Project', {'fields': ['proj_name', 'proj_file']}),
        ('Date information', {'fields': ['upload_date', 'expire_date']}),
    ]

admin.site.register(Project, ProjectAdmin)
