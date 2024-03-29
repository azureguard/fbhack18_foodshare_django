from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('group_buy/', views.group_buy, name='group_buy'),
    path('sharing/', views.sharing, name='sharing'),
    path('group_buy/details', views.details, name='details'),
    path('sharing/details', views.details, name='details'),
    path('<int:user_id>/', views.user_details, name='profile'),
]