from rest_framework.serializers import ModelSerializer
from .models import Employee
# create serializer class


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        # exclude = ['id', ]
