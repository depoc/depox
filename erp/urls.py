from django.urls import path

from . import views

app_name = 'erp'
urlpatterns = [
    path('', views.erp, name='index'),

    path('excluir/', views.Settings.account_delete, name='delete'),

    path(
        'membro/<int:pk>/excluir',
         views.Settings.member_delete, 
         name='member_delete'
    ),

    path(
        'alterar-senha/',
        views.Settings.PasswordChange.as_view(),
        name='password_change',
    ),
]
