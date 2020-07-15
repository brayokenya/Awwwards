from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'user', 'bio']
        
class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['url', 'developer', 'pub_date']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']