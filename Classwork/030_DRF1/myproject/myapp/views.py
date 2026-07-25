from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import *
from myapp.serilizer import *

# Create your views here.

@api_view(['GET'])
def list_student(request):
    students = Student.objects.all()
    ser = StudentSerilizer(students,many=True)
    return Response({'data':ser.data})

@api_view(['POST'])
def create_student(request):
    ser = StudentSerilizer(data=request.data)
    if not ser.is_valid():
        return Response({'errors':ser.errors,"message":'something went wrong!..'})
    else:
        ser.save()
        return Response({'data':ser.data})

@api_view(['DELETE'])
def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return Response("Student Deleted Successfully!...")

@api_view(['PUT'])
def update_student(request,id):
    student = Student.objects.get(id=id)
    ser = StudentSerilizer(student,request.data)
    if not ser.is_valid():
        return Response({'errors':ser.errors,"message":'something went wrong!..'})
    else:
        ser.save()
        return Response({'data':ser.data})

@api_view(['PATCH'])
def patch_student(request,id):
    student = Student.objects.get(id=id)
    ser = StudentSerilizer(student,request.data)
    if not ser.is_valid():
        return Response({'errors':ser.errors,"message":'something went wrong!..'})
    else:
        ser.save()
        return Response({'data':ser.data})
