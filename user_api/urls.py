from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views.register import UserRegistrationView
from .views.token import CustomTokenObtainPairView
from .views.users import UserAddOrListView
from .views.profile import UserProfileUpdateOrDeleteView


urlpatterns = [
    # POST: {base}/user/sign-up/
    path(
        route="sign-up/", view=UserRegistrationView.as_view(), name="user_signup"
    ),
    # POST: {base}/user/token/
    path(
        route="token/", view=CustomTokenObtainPairView.as_view(), name="user_token"
    ),
    # POST: {base}/user/token/refresh/
    path(
        route="token/refresh/", view=TokenRefreshView.as_view(), name="user_token_refresh"
    ),
    # POST GET: {base}/user/add-or-list/
    path(
        route="add-or-list/", view=UserAddOrListView.as_view(), name="user_add_or_list"
    ),
    # PATCH DELETE: {base}/user/update-or-delete/
    path(
        route="update-or-delete/", view=UserProfileUpdateOrDeleteView.as_view(), name="user_update_or_delete"
    ),
]
