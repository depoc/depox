from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'erp'
urlpatterns = [
    path('', views.erp, name='index'),

    path(
        'alterar-senha/',
        auth_views.PasswordChangeView.as_view(),
        name='password_change',
    ),
]
