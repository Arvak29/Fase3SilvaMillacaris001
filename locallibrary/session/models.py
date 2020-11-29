'''from django.contrib.auth.models import AbstractBaseUser, BaseUserManager'''
from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='user.png')

    def __str__(self):
        return f'Perfil de {self.user.username}'

'''
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True)

    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.username} {self.email}'


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email adress")
        if not username:
            raise ValueError("Users must have an email adress")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
    
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.model(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_module_perms(self, app_Label):
        return True
'''

