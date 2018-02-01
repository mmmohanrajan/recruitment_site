from django.shortcuts import render

from rest_framework.response import Response as res
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from api.v1.models import JobPost, Employee
from api.v1.serializers import JobPostSerializer, EmployeeSerializer


class OpeningsAPIView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing Openings.

    post:
    Create a new Openings instance.
    """
    queryset = JobPost.objects.all()  
    serializer_class = JobPostSerializer

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

class OpeningsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return a single openings details.

    update:
    Update opeings instant.

    delete:
    Delete opeings instant.
    """
    queryset = JobPost.objects.all()  
    serializer_class = JobPostSerializer
        

class ApplicationAPIView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing Applications.

    post:
    Create a new Application instance.
    """    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (AllowAny,)

class ApplicationDetailAPIView(generics.RetrieveAPIView):
    """
    get:
    Return a details about single Application instant.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ApplicationAcceptAPIView(APIView):
    """
    patch:
    Used to make application accept or reject.
    """
    def get_object(self, pk):
        return Employee.objects.get(pk=pk)

    def patch(self, request, pk):
        app_model = self.get_object(pk)
        serializer = EmployeeSerializer(app_model, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return res(status=200, data=serializer.data)
        return res(status=400, data={})