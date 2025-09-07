from django.contrib import admin

from .models import Rate


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('score', 'movie', 'user', 'created_at')
    search_fields = ('movie__title', 'user__username')
    list_filter = ('score', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
