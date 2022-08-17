from django.contrib import admin

from .models import Project

class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'flare', 'github_link', )

admin.site.register(Project, HomeAdmin)
