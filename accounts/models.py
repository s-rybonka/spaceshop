from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password=password, **extra_fields)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(**{'{}__iexact'.format(self.model.USERNAME_FIELD): username})


class Account(AbstractBaseUser):
    """Auth user"""

    email = models.EmailField(verbose_name=_('Email'), max_length=255, unique=True)

    username = models.CharField(max_length=30, unique=True, null=True, verbose_name=_('User name'))

    is_active = models.BooleanField(_('Site access'), default=True)

    is_staff = models.BooleanField(_('Admin access'), default=False)

    is_email_confirmed = models.BooleanField(_('Email confirmed'), default=False)

    date_joined = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.username

    def check_telephone_is_confirmed(self):
        return self.is_telephone_confirmed

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return self.is_staff

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return self.is_staff
