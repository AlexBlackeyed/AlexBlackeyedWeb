from django.contrib import admin

from .models import Post

class HomeAdmin2(admin.ModelAdmin):
    list_display = ('post_title','post_url_title')

admin.site.register(Post, HomeAdmin2)
