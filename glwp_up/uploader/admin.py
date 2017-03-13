from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Project, User


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('proj_name', 'user', 'proj_file', 'upload_date', 'expire_date')
    fieldsets = [
        ('User', {'fields': ['user']}),
        ('Project', {'fields': ['proj_name', 'proj_file']}),
        ('Date information', {'fields': ['upload_date', 'expire_date']}),
    ]


class MyUserAdmin(UserAdmin):
    list_display = ('username', 'num_of_projects')
    fieldsets = [
        ('User', {'fields': ['username', 'first_name', 'last_name', 'password']}),
        ('Projects', {'fields': ['num_of_projects']}),
    ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(User, MyUserAdmin)
