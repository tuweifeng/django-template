import re
from django.db import models
from base.models import AabstractAuthor, AbstractAccount, AabstractVideo, AabstractVideoProfile

# Create your models here.


class Account(AbstractAccount):
    pass


class Author(AabstractAuthor):
    def get_mid(self) -> str:
        # https://space.bilibili.com/1574641450?spm_id_from=333.1007.tianma.1-2-2.click
        pattern = re.search(r"https://space.bilibili.com/(\d+)", self.space)
        if pattern:
            mid = pattern.groups(1)[0]
            return mid


class Video(AabstractVideo):
    author = models.ForeignKey(
        to=Author, on_delete=models.CASCADE, null=False, blank=False)

    def get_bvid(self) -> str:
        pattern = re.search(r"https://www.bilibili.com/video/(\w+)", self.url)
        if pattern:
            bvid = pattern.groups(1)[0]
            return bvid


class VideoProfile(AabstractVideoProfile):
    video = models.ForeignKey(
        to=Video, on_delete=models.CASCADE, related_name="profile", null=False, blank=False)
