from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Usuario(AbstractUser):
    password = models.CharField(max_length=50, default='123456abc!')
    username = models.CharField(max_length=50, default='username', unique=True)
    def __str__(self):
        return f'''
            {self.first_name} 
            {self.last_name}       
        '''

    
