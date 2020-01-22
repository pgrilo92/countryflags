from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flags/<int:flag_id>/', views.flags_detail, name='detail'),
    path('flags/', views.flags_index, name='index'),
    path('about/', views.about, name='about'),
    path('flags/create/', views.FlagCreate.as_view(), name='flags_create'),
    path('flags/<int:pk>/update/', views.FlagUpdate.as_view(), name='flags_update'),
    path('flags/<int:pk>/delete/', views.FlagDelete.as_view(), name='flags_delete')
]