from django.contrib import admin

from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'user', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('release_date', 'created_at', 'user')
    ordering = ('-release_date', '-created_at')
    readonly_fields = ('created_at', 'updated_at')
