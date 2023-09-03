from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path("login/", views.login),
    path("user/", views.get_user_data),
    path("register/", views.register),
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
]
