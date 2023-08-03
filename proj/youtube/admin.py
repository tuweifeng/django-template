from django.contrib import admin
from .models import Account, Author, Video
from base.admin import ListAllModelAdmin


# Register your models here.
admin.site.register(Account, ListAllModelAdmin)
admin.site.register(Author, ListAllModelAdmin)
admin.site.register(Video, ListAllModelAdmin)
