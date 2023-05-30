from django.contrib.auth.models import AbstractBaseUser,AbstractUser, PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    objects = UserManager()

    def save(self, *args, **kwargs):
        try:
            super(User, self).save(*args, **kwargs)
        except Exception:
            print("failed to save User changes")
        
    
    USERNAME_FIELD = "username"
    
    # REQUIRED_FIELDS = []

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.email