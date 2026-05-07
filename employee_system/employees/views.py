from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializer


# Add Employee + Get Active Employees
class EmployeeListCreateView(APIView):

    def get(self, request):
        employees = Employee.objects.filter(status='ACTIVE')
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


# Fetch by ID + Update + Soft Delete
class EmployeeDetailView(APIView):

    def get_object(self, pk):
        try:
            return Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return None

    def get(self, request, pk):
        employee = self.get_object(pk)

        if not employee:
            return Response({"error": "Not found"}, status=404)

        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = self.get_object(pk)

        if not employee:
            return Response({"error": "Not found"}, status=404)

        serializer = EmployeeSerializer(
            employee,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        employee = self.get_object(pk)

        if not employee:
            return Response({"error": "Not found"}, status=404)

        employee.status = 'INACTIVE'
        employee.save()

        return Response({
            "message": "Employee soft deleted"
        })