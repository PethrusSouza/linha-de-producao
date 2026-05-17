from django.urls import path
from core import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('dashboard/', views.dashboard_page, name='dashboard'),
    path('itens/', views.itens_page, name='itens-page'),
    path('usuarios/', views.usuarios_page, name='usuarios'),
    path('api/itens/', views.itens_api, name='itens-api'),
]
