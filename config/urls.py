from django.contrib import admin
from django.urls import path

from app.views import list_view, teams, parent

urlpatterns = [
    path("", list_view),
    path("<str:team_num>", teams),
    path("admin/", admin.site.urls),
]
