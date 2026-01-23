from django.urls import path
from users.views.sign_in_user_api_view import SignInUserApiView
from users.views.user_id_api_view import UserIdApiView
from users.views.refresh_token_api_view import RefreshTokenApiView

urlpatterns = [
    path("sign-in/", SignInUserApiView.as_view(), name="sign-in-user"),
    path("user-id/", UserIdApiView.as_view(), name="user-id"),
    path("refresh-token/", RefreshTokenApiView.as_view(), name="refresh-token"),
]
