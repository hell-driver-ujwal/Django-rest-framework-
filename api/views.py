from students.models import Student
from .serializers import StudentSearializer, EmplpyeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from employees.models import Employee

from rest_framework.views import APIView

# Create your views here.

@api_view(['GET','POST'])
def studentsView(request):
    if request.method == 'GET':
        # Get all the data from students table
        students = Student.objects.all()
        serializer = StudentSearializer(students, many =True )

        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSearializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def studentDetailView(request, pk):
    student = get_object_or_404(Student,id = pk)
    if request.method == "GET":
        searializer = StudentSearializer(student)
        return Response(searializer.data, status = status.HTTP_200_OK)
    
    elif request.method == "PUT":
        searializer = StudentSearializer(student, data = request.data)
        if searializer.is_valid():
            searializer.save() 
            return Response(searializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(searializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        student.delete()
        return Response(searializer.data, status = status.HTTP_202_ACCEPTED)

class Employees(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serilizer = EmplpyeeSerializer(employees, many = True)
        return Response(serilizer.data, status = status.HTTP_200_OK)
    def post(self, request):
        searializer = EmplpyeeSerializer(data = request.data)
        if searializer.is_valid():
            searializer.save()
            return Response(searializer.data, status = status.HTTP_201_CREATED )
        return Response(searializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EmployeeDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Employee, pk = pk)
     
    def get(self,request, pk):
        employee = self.get_object(pk = pk)
        searializers = EmplpyeeSerializer(employee)
        return Response(searializers.data, status = status.HTTP_200_OK)
    
    def put(self, request, pk):
        employee = self.get_object(pk = pk)

        serializers = EmplpyeeSerializer(employee, data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_202_ACCEPTED)
        return  Response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self ,request, pk):
        employee = self.get_object(pk = pk)
        # serilizer = EmplpyeeSerializer(employee)
        employee.delete()
        return Response(status = status.HTTP_202_ACCEPTED)

  