from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Rate
from .serialzers import RateCreateSerializer, RateSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = RateSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['score',]

    def get_serializer_class(self):
        if self.action == 'create':
            return RateCreateSerializer
        return super().get_serializer_class()
