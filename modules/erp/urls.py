from django.urls import path

from . import views

app_name = 'erp'
urlpatterns = [
    path('', views.erp, name='index'),

    path('conta/excluir/', views.account_delete, name='account_delete'),

    path('membro/<int:pk>/excluir', views.member_delete, name='member_delete'),

    path(
        'alterar-senha/',
        views.PasswordChange.as_view(),
        name='password_change',
    ),
]
