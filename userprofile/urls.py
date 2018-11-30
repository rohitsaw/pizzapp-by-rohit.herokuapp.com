from django.urls import path
from . import views


app_name = 'userprofile'

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("new_user", views.new_user, name="new_user"),
    path("signup", views.signup, name="signup"),
    path("editprofile", views.editprofile, name="editprofile"),
    path("doedit", views.doedit, name="doedit")
]
