from typing import Sequence
from .models import Account, Video, Author, VideoProfile
from base.models import AabstractVideo
from base.manager import AbstractVideoManager
from django.db import close_old_connections
from yt_dlp import YoutubeDL


class VideoManager(AbstractVideoManager):
    APP_LABEL = "youtube"

    def __init__(self, account: Account = None) -> None:
        self.account = account

    def download(self, video: Video, output: str = None) -> str:
        if not output:
            output = self.FILES_ROOT + '/%(uploader)s/%(title)s.%(ext)s'

        def _hook_progress(info):
            if info['status'] == 'finished' and info["filename"].endswith(".mp4"):
                close_old_connections()
                video.file = info["filename"]
                video.save()

        ydl_opts = {
            "proxy": "clash:7890",
            "outtmpl": output,
            "format": "mp4",
            "subtitlesformat": "vtt",
            "subtitleslangs": ["zh-TW", "yue-HK", "zh-Hans", "zh-Hant"],
            "writesubtitles": True,
            "writeautomaticsub": True,
            'progress_hooks': [_hook_progress],
        }

        with YoutubeDL(ydl_opts) as dl:
            dl.download([video.url])
        return video.file.path

    def reprint(self, video: AabstractVideo, tid: int = None) -> dict:
        pass

    def fetch(self, author: Author, limit=3) -> Sequence[Video]:

        ydl_opts = {
            'playliststart': 0,
            'playlistend': limit,
            'format': "[height <=? 144]",
            "proxy": "clash:7890",
            'list_thumbnails': False,
            'extract_flat': True
        }

        with YoutubeDL(ydl_opts) as dl:
            data = dl.extract_info(author.space, download=False)

        close_old_connections()

        tag = ",".join(data["tags"] or [])
        channel = data["channel"]

        videos = []

        for item in data["entries"]:
            video = Video.objects.create(
                url=item["url"],
                title=item["title"],
                duration=item["duration"],
                author=author
            )
            video.save()

            video_profile = VideoProfile.objects.create(
                video=video,
                tag=tag,
                channel=channel,
                description=item["description"]
            )
            video_profile.save()
            videos.append(video)

        return videos
