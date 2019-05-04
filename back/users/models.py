from django.db import models
from django.contrib.auth.base_user import (AbstractBaseUser,
                                           BaseUserManager)
from datetime import datetime


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('The give email must be set')

        user = self.model(email=email,
                          is_staff=is_staff,
                          is_active=True,
                          is_superuser=is_superuser,
                          date_joined=datetime.now(),
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password,
                                 False,
                                 False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email,
                                 password,
                                 True,
                                 True,
                                 **extra_fields)


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField('Emailaddress', unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    send_email_for_downtime = models.BooleanField(default=True)
    send_email_for_issues = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super(User, self).save(*args, **kwargs)
