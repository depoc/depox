from django.urls import path

from . import views


app_name = 'finance'
urlpatterns = [
    path('', views.caixa, name='caixa'),
    path(
        'lancamento/<int:pk>/excluir/',
        views.delete_transaction,
        name='delete_transaction',
    ),
]
