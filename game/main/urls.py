from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('main/Lv1.html/', views.Lv1),
    path('main/Lv1.html/Lv2.html', views.Lv2),
    path('main/Lv1.html/Lv3.html', views.Lv3),
    path('main/Lv1.html/Lv4.html', views.Lv4),
    path('main/Lv1.html/Lv5.html', views.Lv5),
    path('main/Lv1.html/Lv6.html', views.Lv6),
    path('main/Lv1.html/Lv7.html', views.Lv7),
    path('main/Lv1.html/Lv8.html', views.Lv8),
    path('main/Lv1.html/Result.html', views.Result),
    path('main/Lv1.html/Main.html', views.Result),
]
