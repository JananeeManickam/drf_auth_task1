from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email is not given.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff = True")

        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser = True")
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=128, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #other permissions for users
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True


# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# # Create your models here.

# class UserManager():
#     def create(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError("Email not provided!")
#         email = self.normalize_email(email)
#         user = self.model(email = email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
    
#     def create_superuser(self, email, password, **extra_fields):
#         #super user has all permission
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
        
#         if not extra_fields.get('is_staff'):
#             raise ValueError("Superuser must be a true value for is_staff")
        
#         if not extra_fields.get('is_superuser'):
#             raise ValueError("Superuser must be a true value for is_superuser")
        
#         return self.create_user(email, password, **extra_fields)
    
    
# class CustomUser(AbstractBaseUser):
#     username = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100, unique=True)
#     password = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=12)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     #user permission fields
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
    
#     USERNAME_FIELD = 'email'
#     #req field not needed
    
#     objects = UserManager()
    
#     def __str__(self):
#         return self.email