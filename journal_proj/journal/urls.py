from django.urls import path
from . import views

urlpatterns = [
    path('', views.reg),
    path('auth/', views.authoriz),
    path('reg/', views.reg),
    path('main/', views.main),
    path('write/', views.writing),
    path('jour/', views.read_jour)

]