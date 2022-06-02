from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from base.models import Proffession

#manager for our custom model 
class MyAccountManager(BaseUserManager):
    """
        This is a manager for Account class 
    """
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an Email address")
        if not username :
            raise ValueError("Users must have an Username")
        user  = self.model(
                email=self.normalize_email(email),
                username=username,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username,
            )
        user.is_admin = True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    
    """
      Custom user class inheriting AbstractBaseUser class 
    """
    first_name           = models.CharField(max_length=120)
    last_name            = models.CharField(max_length=120)
    email                = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username             = models.CharField(max_length=30,unique=True)
    proffession          = models.ForeignKey(Proffession, on_delete=models.SET_NULL, null=True)
    date_joined          = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login           = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin             = models.BooleanField(default=False)
    is_active            = models.BooleanField(default=True)
    is_staff             = models.BooleanField(default=False)
    is_superuser         = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    class Meta:
        verbose_name_plural = "User"

    def __str__(self):
        return f"Username - {self.username}, date joined - {self.date_joined}"

    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label ):
        return True
