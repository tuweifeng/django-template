from django.db import models
from base.models import AabstractAuthor, AbstractAccount, AabstractVideo, AabstractVideoProfile

# Create your models here.


class Account(AbstractAccount):
    pass


class Author(AabstractAuthor):
    pass


class Video(AabstractVideo):
    author = models.ForeignKey(
        to=Author, on_delete=models.CASCADE, null=False, blank=False)


class VideoProfile(AabstractVideoProfile):
    video = models.ForeignKey(
        to=Video, on_delete=models.CASCADE, related_name="profile", null=False, blank=False)
