from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from account.managers import CustomUserManager
from . import choices

# Create your models here.

class User(AbstractBaseUser):
    first_name = models.CharField(verbose_name='نام', max_length=50)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=50)
    email = models.EmailField(verbose_name='ایمیل', max_length=254,unique=True)
    role = models.CharField(verbose_name='نقش',max_length=50,choices=choices.USER_ROLE_CHOICES)
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال',default=False)
    date_joined = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ عضویت')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    
    objects = CustomUserManager()


    class Meta:
        verbose_name = 'اکانت'
        verbose_name_plural = 'اکانتهای'

    def __str__(self):
        return self.first_name

    @staticmethod
    def has_perm(self, perm='__all__', obj=None):
        return True

    @staticmethod
    def has_module_perms(self, app_label="account"):
        return True

    @property
    def is_staff(self):
        return self.role == choices.USER_ROLE_ADMIN

    @property
    def is_instructor(self):
        return self.role == choices.USER_ROLE_INSTRUCTOR

    @property
    def is_student(self):
        return self.role == choices.USER_ROLE_STUDENT
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'