"""User Role Management URLs."""

from django.urls import path

from . import api

app_name = "admin.user_role_management"

urlpatterns = [
    path("user-profiles/", api.UserProfileList.as_view()),
    path("user-profiles/<int:pk>/", api.UserProfileDetail.as_view()),
    path("roles/", api.RoleList.as_view()),
    path("roles/<int:pk>/", api.RoleDetail.as_view()),
]
