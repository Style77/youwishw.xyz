from django.urls import path

from . import views

urlpatterns = [
    # ex: /music/
    path('', views.index, name='index'),
    # ex: /music/user
    path('user/', views.user, name='user'),
    # ex: /music/12352
    path('<int:song_id>/', views.song_details, name='song_details'),
    # ex: /music/user/4573489
    # path('user/<int:user_id>', views.user_details, name='user_details'),

    path('upload/', views.upload, name='logout'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name="login"),
]