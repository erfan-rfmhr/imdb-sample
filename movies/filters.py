import django_filters.rest_framework as filters
from rest_framework.filters import SearchFilter

from .models import Movie


class MovieFilter(filters.FilterSet):
    release_date = filters.DateFromToRangeFilter()
    created_at = filters.DateFromToRangeFilter()
    user = filters.CharFilter(field_name='user__username', lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['release_date', 'created_at', 'user']

class MovieSearchFilter(SearchFilter):
    search_param = 'q'
