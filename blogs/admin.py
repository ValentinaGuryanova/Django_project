from django.contrib import admin

from blogs.models import Blogs


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    list_filter = ('title',)
    search_fields = ('title', 'body',)