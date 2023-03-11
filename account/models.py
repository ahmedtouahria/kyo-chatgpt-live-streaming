from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
import uuid

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_active=True, admin=False):
        if not email:
            raise ValueError('users must have a email number')
        if not password:
            raise ValueError('user must have a password')
        user_obj = self.model(email=email)
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.admin = admin
        user_obj.save(using=self._db)
        return user_obj
    def create_staffuser(self, email, password=None):
        user = self.create_user(email,password=password,is_staff=True,)
        return user
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            admin=True,
        )
        return user
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            admin=True,
            is_staff=True
        )
        return user

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email = models.EmailField(unique=True,max_length=300)
    full_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="user", blank=True, null=True)
    first_login = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    password=models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return self.full_name
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_active(self):
        return self.active
    @property
    def is_superuser(self):
        return self.admin


class Notification(models.Model):
    user_id=models.ForeignKey("account.user", verbose_name=_("user"), on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=250)
    content = models.TextField(null=True,blank=True)
    is_new = models.BooleanField(default=True)
    def __str__(self):
        return self.title
