from rest_framework import serializers
#from .models import CustomUser
from .models import *

# Company Profile
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_Profile
        fields= ['id','company_name','domain','phone','whatsapp','email','location','industry','employees','employee_growth','revenue','technologies','linkedin','twitter','profile_photo','created_at']
        # fields= ['id','full_name','phone','alt_phone','gender','DOB','profile_photo','created_at','updated_at']