from django.urls import path
from users.views.sign_up_user_api_view import SignUpUserApiView
from users.views.sign_in_user_api_view import SignInUserApiView

urlpatterns = [
    path("sign-up/", SignUpUserApiView.as_view(), name="sign-up-user"),
    path("sign-in/", SignInUserApiView.as_view(), name="sign-in-user"),
]
