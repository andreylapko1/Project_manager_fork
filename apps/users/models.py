from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.db import models, DatabaseError
from django.db.models import ForeignKey


class PositionChoises(models.TextField):
    POSITION_CHOICES = [
        ('CEO', 'Ceo'),
        ('CTO', 'Cto'),
        ('DESIGNER', 'Designer'),
        ('PROGRAMMER', 'Programmer'),
        ('PRODUCT_OWNER', 'Product_owner'),
        ('PROJECT_OWNER', 'Project_owner'),
        ('PROJECT_MANAGER', 'Project_manager'),
        ('QA', 'Qa'),
    ]



class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=40, unique=True)
    last_name = models.CharField(max_length=40, unique=True)
    email = models.CharField(unique=True, max_length=100)
    phone = models.CharField(max_length=75, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=True)
    project = models.ForeignKey('projects.Project', on_delete=models.SET_NULL, null=True, blank=True)
    position = models.CharField(choices=PositionChoises.POSITION_CHOICES, max_length=255, null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
    ]
    objects = UserManager()

