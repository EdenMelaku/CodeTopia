from django.db import models

from django.conf import settings

from django.utils.translation import gettext_lazy as _

import os

__all__ = [ "Blog" ]

class BlogManager(models.Manager):
    """Model Manager for Profile model"""
    def get_queryset(self):
        return super(BlogManager, self).get_queryset().filter(published=True)

def get_profile_pic_path(instance, filename):
    """Method that returns upload location for the current user's profile picture"""
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    file_path = os.path.join("users_profile_pic", instance.user.username, filename)
    return file_path

class Blog(models.Model):

    author = models.OneToOneField(
        to=settings.AUTH_USER_MODEL, 
        verbose_name=_("Author"), 
        on_delete=models.CASCADE
    )

    title = models.CharField(verbose_name=_("Title"), max_length=60)
    subject = models.CharField(verbose_name=_("Subject"), max_length=100)
    body = models.CharField(verbose_name=_("Body"), max_length=1500)
    published = models.BooleanField(verbose_name=_("Published"), default=False)

    objects = models.Manager()
    blogs = BlogManager()

    def __str__(self):
        return "%s"% self.author.username
