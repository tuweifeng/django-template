from typing import Sequence
from django.contrib import admin
from django.http.request import HttpRequest


class ListAllModelAdmin(admin.ModelAdmin):
    list_display = []

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    def get_list_display(self, request: HttpRequest) -> Sequence[str]:
        return super().get_list_display(request) or [field.attname for field in self.model._meta.fields]
