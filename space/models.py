from pyexpat import model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100, default=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=12)
    confirm_password = models.CharField(max_length=12)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    email_plaintext_message = "{} token={} {}\n{} {}".format("Your Password Reset " , reset_password_token.key, "(copy this token id)", "Click the given url and Enter Token ", " http://127.0.0.1:8000/space/api/password_reset/confirm/")
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Reset Password"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
    
gender= (
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other")
)
class User_Profile(models.Model):
    full_name=models.CharField(max_length=200)
    phone = models.IntegerField(blank=False, unique=True)
    alt_phone = models.IntegerField(blank=False)
    gender = models.CharField(max_length=100,choices=gender)
    DOB = models.DateField(auto_now_add=True) 
    profile_photo = models.ImageField(upload_to='register/image', blank=True)
    # address = models.CharField(max_length=200)
    # city =models.CharField(max_length=200)
    # state = INStateField(null=True, blank=True)
    # pincode = models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.full_name)
