from typing import Sequence
from .models import Account, Video, Author
from base.models import AabstractVideo
from base.manager import AbstractVideoManager
from django.db import close_old_connections
from someapi.custom.bilibili import upload_video, download_delogo_video, get_user_videos


class VideoManager(AbstractVideoManager):
    APP_LABEL = "bilibili"

    def __init__(self, account: Account = None) -> None:
        self.account = account

    def download(self, video: Video, output: str = None) -> str:
        if not output:
            output = self.FILES_ROOT + \
                f"/{video.author.nickname}/{video.title}.mp4"
        download_delogo_video(
            video.url, output, cookies=self.account.cookies if self.account else None)
        close_old_connections()
        video.file = output
        video.save()
        return output

    def reprint(self, video: AabstractVideo, tid: int = None) -> dict:
        return upload_video(self.account.cookies, video.file.path,
                            video.title, tid, video.profile.tag, source=video.url, copyright=2)

    def fetch(self, author: Author, limit=3) -> Sequence[AabstractVideo]:
        data = get_user_videos(author.get_mid(), 1, page_size=limit)
        close_old_connections()
        videos = []
        for item in data["data"]["list"]["vlist"]:
            video = Video.objects.create(
                url=f'https://www.bilibili.com/video/{item["bvid"]}',
                title=item["title"],
                duration=sum(
                    [int(v)*60**i for i, v in enumerate(item["length"].split(":")[::-1])]),
                author=author
            )
            video.save()
            videos.append(video)

        return videos
