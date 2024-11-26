from rest_framework import viewsets
from .models import NetworkNode
from .serializers import NetworkNodeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions


class IsActiveEmployee(permissions.BasePermission):
    """
    Разрешение для активных сотрудников
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_active


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveEmployee]  #

    def get_queryset(self):
        """
        Фильтрация по стране
        """
        queryset = super().get_queryset()
        country = self.request.query_params.get('country', None)
        if country:
            queryset = queryset.filter(country=country)
        return queryset

    def perform_update(self, serializer):
        """
        Запрещаем обновление поля задолженности перед поставщиком
        """
        debt = serializer.validated_data.get('debt', None)
        if debt is not None:
            serializer.validated_data.pop('debt')
        serializer.save()
