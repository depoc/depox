from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.contacts, name='main'),
    path('edit/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('excluir/<int:pk>/', views.delete_contact, name='delete_contact'),
]
