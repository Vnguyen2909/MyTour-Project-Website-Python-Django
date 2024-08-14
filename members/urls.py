from django.urls import path
from . import views

app_name = "members"

urlpatterns = [
    path("login_user", views.login_user, name="login"),
    path("logout_user", views.logout_user, name="logout"),
    path("register_user", views.register_user, name="register_user"),
    path("info_user", views.edit_profile, name="edit_profile"),
    path("all_user", views.all_user, name="all-user"),
    path("update_user/<user_id>", views.update_user, name="update-user"),
]
