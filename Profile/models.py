from django.db import models

# Create your models here.
class User_Profile(models.Model):

    full_name = models.CharField(max_length=200)
    stream = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)  
    skills = models.CharField(max_length=200) 
    experience = models.IntegerField() 
    company = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=13,blank=True,null=True)
    whatsapp = models.CharField(max_length=13,blank=True,null=True)
    email = models.EmailField(max_length=200,unique=True)
    address = models.CharField(max_length=500,null=True)
    linkedin = models.URLField(max_length=200,unique=True)
    twitter = models.URLField(max_length=200,unique=True,null=True)
    github = models.URLField(max_length=200,unique=True,null=True)
    gender = models.CharField(max_length=100)
    DOB = models.DateField() 
    profile_photo = models.ImageField(upload_to='profileimg/', blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.full_name)