from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import NetworkNode
from .serializers import NetworkNodeSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        country = self.request.query_params.get("country")
        if country:
            return self.queryset.filter(country=country)
        return self.queryset
