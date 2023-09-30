from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("macroindex/<int:topic_id>/", views.macroindex, name="macroindex"),
    path("macroindex", views.main_macroindex, name="main_macroindex"),
    path("economic_index/<int:economic_index_id>/", views.economic_index, name="economic_index"),
    path("logout_user", views.logout_user, name="logout_user")
]
