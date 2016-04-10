#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils.translation import ugettext_lazy as _
from django.core import validators


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, mobile, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('请输入用户名')
        # if not mobile:
        #     raise ValueError('请输入手机号码')
        if mobile:
            mobile = self.normalize_mobile(mobile)
        user = self.model(username=username, mobile=mobile,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, mobile=None, password=None, **extra_fields):
        return self._create_user(username, mobile, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, mobile=None, password=None, **extra_fields):
        return self._create_user(username, mobile, password, True, True,
                                 **extra_fields)

    @classmethod
    def normalize_mobile(cls, mobile):
        return mobile.replace("-", "").strip()


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """
    用户基本信息
    http://python.usyiyi.cn/django/topics/auth/customizing.html#extending-user
    """
    username = models.CharField(_('username'), max_length=64, unique=True,
                                help_text=_('5~30个字母，数字或@/./+/-/_字符。'),
                                validators=[
                                    validators.RegexValidator(r'^[\w.@+-]{5,30}$',
                                                              _('输入有效的用户名。 '
                                                                '包含5~30个字母，数字或@/./+/-/_字符。'), 'invalid'),
                                ],
                                error_messages={
                                    'unique': _("A user with that username already exists."),
                                })
    first_name = models.CharField(_('first name'), max_length=30, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True, null=True)
    email = models.EmailField(_('email address'), blank=True, null=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    mobile = models.CharField("手机号", help_text="手机号", max_length=15, blank=True, null=True)
    nick_name = models.CharField("昵称", help_text="昵称", max_length=30, unique=True, blank=True, null=True)
    remark = models.CharField("个性签名", help_text="个性签名", max_length=300, blank=True, null=True)
    image = models.CharField("头像", help_text="头像图片URL路径", max_length=300, blank=True, null=True)
    wechat = models.CharField("微信号", help_text="微信号", max_length=100, blank=True, null=True)
    wechat_open_id = models.CharField("微信OpenId", help_text="微信OpenId", max_length=100, blank=True, null=True)
    date_of_birth = models.DateField("生日", help_text="生日", blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = "checknow_users"

    backend = "django.contrib.auth.backends.ModelBackend"

    def _get_full_name(self):
        """Returns the person's full name."""
        if self.first_name and self.last_name:
            return '%s%s' % (self.first_name, self.last_name)
        elif self.nick_name:
            return self.nick_name
        elif self.username:
            return self.username
        elif self.mobile:
            return self.mobile
        else:
            return "User%s" % self.id

    full_name = property(_get_full_name)

    def __unicode__(self):
        return self._get_full_name()


class AuthProfile(models.Model):
    # 必选
    user = models.OneToOneField(User)
