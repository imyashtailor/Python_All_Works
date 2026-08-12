from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from myapp.serializers import *
from myapp.permissions import *
from rest_framework.permissions import AllowAny

# Create your views here.

@api_view(['POST'])
def reg(request):
    ser = UserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response({'message':'Registration Successfully!...'})

@api_view(['GET'])
@permission_classes([IsStudent])
def get_student(request):
    return Response("Student API Calling...")

@api_view(['GET'])
@permission_classes([IsFaculty])
def get_faculty(request):
    return Response("Faculty API Calling....")

@api_view(['GET'])
@permission_classes([AllowAny])
def get_normal(request):
    return Response("Normal API Calling....")