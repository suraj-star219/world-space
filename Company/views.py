from rest_framework import generics, permissions
from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework.generics import ListCreateAPIView
from rest_framework.filters import OrderingFilter,SearchFilter
from .serializers import *
from .models import *
# Create your views here.
class CompanyProfileViewSet(viewsets.ModelViewSet):
    #permission_classes=[IsAuthenticated]
    permission_classes = (permissions.AllowAny,)
    queryset = Company_Profile.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter]
    search_fields = ['id','company_name','domain','phone','whatsapp','email','location','industry','employees','employee_growth','revenue','technologies','linkedin','twitter','profile_photo','created_at']

    def put(self, request, id, format=None):
            company = self.get_object(id=id)
            serializer = CompanySerializer(company, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
            company = self.get_object(id=id)
            serializer = CompanySerializer(company, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        