import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class AbstractAccount(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nickname = models.CharField(verbose_name=_(
        "nickname"), max_length=200, null=False, blank=False)
    space = models.URLField(null=False, blank=False)
    cookies = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("account")
        db_table = "account"
        abstract = True


class AabstractAuthor(models.Model):
    nickname = models.CharField(verbose_name=_(
        "nickname"), max_length=200, null=False, blank=False)
    space = models.URLField(null=False, blank=False)

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("author")
        db_table = "author"
        abstract = True


class AabstractVideo(models.Model):
    url = models.URLField(null=False, blank=False)
    title = models.CharField(verbose_name=_(
        "title"), max_length=200, null=False, blank=False)
    author = models.ForeignKey(
        to=AabstractAuthor, on_delete=models.CASCADE, null=False, blank=False)
    file = models.FileField(null=True, blank=True)
    duration = models.IntegerField(
        null=False, blank=False, help_text=_("seconds"))

    class Meta:
        verbose_name = _("video")
        verbose_name_plural = _("video")
        db_table = "video"
        abstract = True


class AabstractVideoProfile(models.Model):
    video = models.ForeignKey(
        to=AabstractVideo, on_delete=models.CASCADE, null=False, blank=False)
    tag = models.TextField(verbose_name=_(
        "tag"), null=True, blank=True)
    description = models.TextField(verbose_name=_(
        "description"), null=True, blank=True)
    channel = models.CharField(verbose_name=_(
        "channel"), max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = _("video profile")
        verbose_name_plural = _("video profile")
        db_table = "video_profile"
        abstract = True
