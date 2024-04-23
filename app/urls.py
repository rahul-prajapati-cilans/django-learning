from django.urls import path

from app.views import UserList, UserDetail

urlpatterns = [
    path("users/", UserList.as_view(), name="user_url"),
    path("users-detail/<int:pk>/", UserDetail.as_view(), name="user_detail"),
]
