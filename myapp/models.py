from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations=True

    def create_user(self, email, password=None, **extra):
        if not email:
            raise ValueError("Email is required")
        user=self.model(email=email, **extra)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra):
        extra.setdefault("is_active", True)
        extra.setdefault("is_staff", True)
        extra.setdefault("is_superuser", True)

        return self.create_user(email,password, **extra)

class User(AbstractBaseUser):
    username = None
    email=models.EmailField(max_length=35, null=False, blank=False, unique=True)
    phone_number=models.CharField(max_length=20, null=False, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD='email'

    objects = UserManager()



