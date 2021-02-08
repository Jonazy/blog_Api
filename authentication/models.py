from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, is_active=True,
                    is_author=True, is_staff=False, is_admin=False, **extra_fields):
        if not email:
            raise ValueError('Please enter email')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.active = is_active
        user.author = is_author
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password=password,
                                is_staff=True, is_admin=True, **extra_fields
                                )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)
    author = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_author(self):
        return self.author

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff
