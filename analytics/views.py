from .serialzers import RateSerializer
from .models import Rate
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = RateSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['score',]
