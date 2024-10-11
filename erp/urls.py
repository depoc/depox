from django.urls import path

from . import views

app_name = 'erp'
urlpatterns = [
    path('', views.erp, name='index'),

    path(
        'alterar-senha/',
        views.Settings.PasswordChange.as_view(),
        name='password_change',
    ),
]
