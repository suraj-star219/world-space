from rest_framework import serializers
#from .models import CustomUser
from .models import *

# User Profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Profile
        fields= ['id','full_name','stream','university','degree','job_title','skills','experience','company','phone','whatsapp','email','address','linkedin','twitter','github','gender','DOB','profile_photo','created_at']
        # fields= ['id','full_name','phone','alt_phone','gender','DOB','profile_photo','created_at','updated_at']
