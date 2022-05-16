from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from testApp.views import (
    RegisterView,
    ContactCreateAPIView,
    ContactListAPIView,
    ContactRetrieveAPIView,
    ContactUpdateAPIView,
    ContactDestroyAPIView,
    GroupAdd,
    GroupDetailView,
    GroupView,
)

urlpatterns = [
    # Login APIs
    path("register/", RegisterView.as_view(), name="auth_register"),
    path("auth-jwt/", obtain_jwt_token),
    path("auth-jwt-refresh/", refresh_jwt_token),
    path("auth-jwt-verify/", verify_jwt_token),
    # Contact APIs
    path("create-contact/", ContactCreateAPIView.as_view(), name="create-contact"),
    path("contacts/", ContactListAPIView.as_view(), name="list-contact"),
    path("contact/<int:pk>", ContactRetrieveAPIView.as_view(), name="retrieve-contact"),
    path("update-contact/<int:pk>", ContactUpdateAPIView.as_view(), name="update-contact"),
    path("delete-contact/<int:pk>", ContactDestroyAPIView.as_view(), name="delete-contact"),
    # Group APIs
    path("group/", GroupAdd.as_view(), name="create-group"),
    path("group/<int:pk>", GroupDetailView.as_view(), name="group_detail"),
    path("groups/", GroupView.as_view(), name="getall-group"),
]
