from django.urls import path

from .views.register import UserRegistrationView


urlpatterns = [
    # POST: {base}/user/sign-up/
    path(
        route="sign-up/", view=UserRegistrationView.as_view(), name="user_signup"
    ),
]
