from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.signin, name='login'),
    path('cadastro/', views.register, name='register'),
    
    path(
        'sair/',
        LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL),
        name='logout'
    ),
]
