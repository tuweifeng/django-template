from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .manager import VideoManager
from .models import Author, Video
# Create your views here.


class VideoView(ViewSet):
    @action(methods=["GET"], detail=False)
    def fetch(self, request):
        manager = VideoManager()
        author = Author.objects.first()
        manager.fetch(author)
        return Response()

    @action(methods=["GET"], detail=False)
    def download(self, request):
        manager = VideoManager()
        video = Video.objects.first()
        path = manager.download(video)
        return Response(data=path)
