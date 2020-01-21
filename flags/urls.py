from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('<int:flag_id>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
]