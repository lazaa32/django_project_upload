from django.contrib import admin
from .models import User, Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('proj_name', 'proj_file', 'upload_date', 'expire_date')
    fieldsets = [
        ('User', {'fields': ['user']}),
        ('Project', {'fields': ['proj_name', 'proj_file']}),
        ('Date information', {'fields': ['upload_date', 'expire_date']}),
    ]
    # fields = ['proj_id', 'proj_name', 'proj_file', 'update_date']

admin.site.register(User)
admin.site.register(Project, ProjectAdmin)
