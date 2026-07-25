from rest_framework import serializers
from myapp.models import *

class StudentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'