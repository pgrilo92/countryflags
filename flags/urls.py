from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flags/<int:flag_id>/', views.flags_detail, name='detail'),
    path('flags/', views.flags_index, name='index'),
    path('about/', views.about, name='about'),
]