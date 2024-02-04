from django.shortcuts import render
from rest_framework import generics
from safecaller import models
from safecaller import serializers

class UserProfileCreateView(generics.CreateAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer

class UserProfileListView(generics.ListAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer

class ContactListView(generics.ListCreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer

class SpamReportCreateView(generics.CreateAPIView):
    queryset = models.SpamReport.objects.all()
    serializer_class = serializers.SpamReportSerializer
    
class SpamReportListView(generics.ListAPIView):
    queryset = models.SpamReport.objects.all()
    serializer_class = serializers.SpamReportSerializer