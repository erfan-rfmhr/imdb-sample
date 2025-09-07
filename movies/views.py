from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .filters import MovieFilter, MovieSearchFilter
from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filterset_class = MovieFilter
    filter_backends = [DjangoFilterBackend, MovieSearchFilter]
    search_fields = ['title', 'description']

    def get_queryset(self):
        return super().get_queryset().order_by('-release_date', '-created_at')
