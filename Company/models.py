from django.db import models

# Create your models here.
class Company_Profile(models.Model):

    company_name = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)  
    phone = models.CharField(max_length=13,blank=True,null=True)
    whatsapp = models.CharField(max_length=13,blank=True,null=True)
    email = models.EmailField(max_length=200,unique=True)
    location = models.CharField(max_length=500,null=True)
    industry = models.CharField(max_length=200)
    employees = models.CharField(max_length=200)
    employee_growth = models.CharField(max_length=200)
    revenue = models.CharField(max_length=200)
    technologies = models.CharField(max_length=200)
    linkedin = models.URLField(max_length=200,unique=True)
    twitter = models.URLField(max_length=200,unique=True,null=True)
    profile_photo = models.ImageField(upload_to='companyimg/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.company_name)