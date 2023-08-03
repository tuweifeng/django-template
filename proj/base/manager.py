import os
from typing import Sequence
from .models import AbstractAccount, AabstractVideo, AabstractAuthor
from base.models import AabstractVideo
from abc import ABC, abstractmethod, abstractproperty
from django.conf import settings


class AbstractVideoManager(ABC):

    @abstractproperty
    def APP_LABEL(self) -> str:
        pass

    @property
    def FILES_ROOT(self) -> str:
        """文件存放目录

        Returns:
            str: 文件存放目录
        """
        root = os.path.join(settings.STATIC_ROOT, self.APP_LABEL, "videos")
        if not os.path.exists(root):
            os.makedirs(root)
        return root

    def __init__(self, account: AbstractAccount = None) -> None:
        self.account = account

    @abstractmethod
    def download(self, video: AabstractVideo, output: str = None) -> str:
        """下载视频

        Args:
            video (Video): 需要包含视频地址信息
            output (str, optional): 下载到该目录, 默认下载到 self.FILES_ROOT

        Returns:
            str: 返回下载完成文件地址
        """
        pass

    @abstractmethod
    def reprint(self, video: AabstractVideo, tid: int = None) -> dict:
        """转载视频

        Args:
            video (AabstractVideo): 需要包含视频地址信息
            tid (int, optional): 投稿到该分区, 默认随机分区

        Returns:
            dict: 返回投稿信息 egg: {"code":0, "message":"0", "ttl":1, "data":{"aid":779951675, "bvid":"BV1Gy4y1o7K1" }}
        """
        pass

    @abstractmethod
    def fetch(self, author: AabstractAuthor, limit=3) -> Sequence[AabstractVideo]:
        """采集视频

        Args:
            author (AabstractAuthor): 需要作者的个人主页地址
            limit (int, optional): 限制采集数量

        Returns:
            Sequence[AabstractVideo]: 返回采集的视频
        """
        pass
