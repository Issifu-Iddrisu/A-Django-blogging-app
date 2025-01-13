from django.urls import path
from . import views


app_name = "main"

urlpatterns  = [
    path("", views.homepage, name="homepage"),
    path("newyear", views.newyear, name="newyear"),
    path("signup", views.signup, name="signup"),
    path("login", views.login_to, name="login"),
    path("logout", views.logout_request, name="logout")
]