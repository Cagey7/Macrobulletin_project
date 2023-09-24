from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("topic/<int:topic_id>/", views.topic, name="topic"),
    path("topic", views.main_topic, name="main_topic"),
    path("economic_index/<int:economic_index_id>/", views.economic_index, name="economic_index"),
    path("logout_user", views.logout_user, name="logout_user")
]
