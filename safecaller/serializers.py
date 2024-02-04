from rest_framework import serializers
from safecaller import models

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ['id', 'user', 'phone_number', 'email']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = "__all__"
    
class SpamReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SpamReport
        fields = "__all__"