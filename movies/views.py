from rest_framework.viewsets import ModelViewSet
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        return super().get_queryset().order_by('-release_date', '-created_at')
