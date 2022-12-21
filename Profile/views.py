from rest_framework import generics, permissions
from django.shortcuts import render
#from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter,SearchFilter
from .serializers import *
from .models import *
# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    #permission_classes=[IsAuthenticated]
    permission_classes = (permissions.AllowAny,)
    queryset = User_Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [SearchFilter]
    search_fields = ['id','full_name','stream','university','degree','job_title','skills','experience','company','phone','whatsapp','email','address','linkedin','twitter','github','gender','DOB','profile_photo','created_at']

    def put(self, request, id, format=None):
        profile = self.get_object(id=id)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        profile = self.get_object(id=id)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    