from . import views
from django.urls import path


app_name = "accounts"
urlpatterns = [
    path("users/admin/", views.CreateAdminView.as_view(), name="create-admin"),
    path("users/", views.UserListView.as_view(), name="user-list"),
    path(
        "users/<int:pk>/",
        views.UserUpdateDetailView.as_view(),
        name="user-detail-update",
    ),
    path("token/", views.LoginView.as_view(), name="token_obtain_pair"),
    path("refresh-token/", views.RefreshTokenView.as_view(), name="token_refresh"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("refresh-token/", views.RefreshTokenView.as_view(), name="refresh-token"),
    path(
        "change-password/", views.ChangePasswordView.as_view(), name="change-password"
    ),
]
