from django.urls import path
from .views import homepage, avatar_upload


urlpatterns = [
    path('', homepage, name="homepage"),
    path('avatar_upload/', avatar_upload, name="avatar_upload"),
]
