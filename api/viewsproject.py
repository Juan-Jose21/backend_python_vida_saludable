from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from api.models import Proyecto
from api.serializers import ProyectoSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "success": True,
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
