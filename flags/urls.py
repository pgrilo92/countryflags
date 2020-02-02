from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flags/<int:flag_id>/', views.flags_detail, name='detail'),
    path('flags/', views.flags_index, name='index'),
    path('about/', views.about, name='about'),
    path('flags/create/', views.FlagCreate.as_view(), name='flags_create'),
    path('flags/<int:pk>/update/', views.FlagUpdate.as_view(), name='flags_update'),
    path('flags/<int:pk>/delete/', views.FlagDelete.as_view(), name='flags_delete'),
    path('flags/<int:flag_id>/add_president/', views.add_president, name='add_president'),
    path('accounts/signup', views.signup, name='signup'),
    path('flags/<int:president_id>/delete_president/', views.delete_president, name='delete_president'),
    path('languages/', views.language_index, name='languages'),
    path('languages/create_language', views.create_language, name='create_language'),
    path('flags/<int:flag_id>/add_language_to_flag/<int:language_id>', views.add_language_to_flag, name='add_language_to_flag'),
    path('flags/<int:flag_id>/remove_language_to_flag/<int:language_id>', views.remove_language_to_flag, name='remove_language_to_flag')
]