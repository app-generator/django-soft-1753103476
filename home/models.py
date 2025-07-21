# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Asset_Type(models.Model):

    #__Asset_Type_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    version = models.IntegerField(null=True, blank=True)

    #__Asset_Type_FIELDS__END

    class Meta:
        verbose_name        = _("Asset_Type")
        verbose_name_plural = _("Asset_Type")


class Asset(models.Model):

    #__Asset_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(asset_type, on_delete=models.CASCADE)

    #__Asset_FIELDS__END

    class Meta:
        verbose_name        = _("Asset")
        verbose_name_plural = _("Asset")



#__MODELS__END
