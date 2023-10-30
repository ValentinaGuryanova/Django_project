from django.contrib import admin

from blogs.models import Blogs


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'is_publish')
    list_filter = ('title', 'is_publish')
    search_fields = ('title', 'body', 'is_publish',)