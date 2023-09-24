from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .authentications import CustomAuthentication, CustomAuthentication_case_2
# Create your views here.


class EmployeeCURDViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    permission_classes = [IsAuthenticated, ]
    authentication_classes = [CustomAuthentication_case_2, ]
