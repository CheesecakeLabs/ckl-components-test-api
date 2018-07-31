from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.is_active = True
        user.is_staff = False
        user.is_superuser = False

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    description = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def natural_key(self):
        return self.email

    def __str__(self):
        return self.email
