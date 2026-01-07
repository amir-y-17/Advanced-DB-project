from rest_framework import status
from .models import Province, City, Village
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from .serializers import ProvinceSerializer, CitySerializer, VillageSerializer


class ProvinceListCreateView(ListCreateAPIView):
    queryset = Province.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProvinceSerializer


class ProvinceDeleteView(DestroyAPIView):
    queryset = Province.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProvinceSerializer

    def delete(self, request, *args, **kwargs):
        province = self.get_object()
        province.delete()
        return Response(
            {"message": "Province deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )


class CityListCreateView(ListCreateAPIView):
    queryset = City.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CitySerializer


class CityDeleteView(DestroyAPIView):
    queryset = City.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CitySerializer

    def delete(self, request, *args, **kwargs):
        city = self.get_object()
        city.delete()
        return Response(
            {"message": "City deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )


class VillageListCreateView(ListCreateAPIView):
    queryset = Village.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = VillageSerializer


class VillageDeleteView(DestroyAPIView):
    queryset = Village.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = VillageSerializer

    def delete(self, request, *args, **kwargs):
        village = self.get_object()
        village.delete()
        return Response(
            {"message": "Village deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
