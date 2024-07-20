from django.urls import path
from users.views.sign_up_user_api_view import SignUpUserApiView
from users.views.sign_in_user_api_view import SignInUserApiView
from users.views.user_id_api_view import UserIdApiView

urlpatterns = [
    path("sign-up/", SignUpUserApiView.as_view(), name="sign-up-user"),
    path("sign-in/", SignInUserApiView.as_view(), name="sign-in-user"),
    path("user-id/", UserIdApiView.as_view(), name="user-id"),
]
